'''
*********************************************************************************************
  *File: IMU_Reading.py
  *Project: IMU_python_reading_3.0
  *Filepath: /home/guoyucan/Downloads/IMU_Python_Reading/IMU_python_reading_3.0/IMU_Reading.py 
  *File Created: Saturday, 18th September 2021 4:41:26 pm
  *Author: Guo Yucan, 12032421@mail.sustech.edu.cn 
  *Last Modified: Wednesday, 22nd September 2021 1:32:13 pm
  *Modified By: Guo Yucan, 12032421@mail.sustech.edu.cn 
  *Copyright @ 2021 , BionicDL LAB, SUSTECH, Shenzhen, China 
*********************************************************************************************
'''

#coding:UTF-8

# For reading data from serial port of IMU module
import serial

# For data collection and recording
from datetime import datetime, time
import csv


# Import the IMU_Plotting_CSV module to plot the imu data
# from IMU_Plotting_CSV import plot_imu_data_csv


## Create a csv file to store the data from IMU

time_mark = datetime.now()

file_name = 'data_' + str(time_mark)

with open( file_name + '.csv','a') as file:
    
    # writer = csv.DictWriter(file, fieldnames=['time','acc_x','acc_y','acc_z','gyro_x','gyro_y','gyro_z','roll','pitch','yaw'])
    # writer.writerow({'time':current,'acc_x':acc_x,'acc_y':acc_y,'acc_z':acc_z,'gyro_x':gyro_x,'gyro_y':gyro_y,'gyro_z':gyro_z,'roll':roll,'pitch':pitch,'yaw':yaw})
    
    writer = csv.writer(file,delimiter=',',quotechar='"',quoting = csv.QUOTE_MINIMAL)
    writer.writerow(['time','acc_x','acc_y','acc_z','roll','pitch','yaw'])

file.close()



## Create parameters to store the temporary data

ACCData=[0.0]*8
GYROData=[0.0]*8
AngleData=[0.0]*8          
FrameState = 0            #通过0x后面的值判断属于哪一种情况
Bytenum = 0               #读取到这一段的第几位
CheckSum = 0              #求和校验位         
 
a = [0.0]*3
w = [0.0]*3
Angle = [0.0]*3

# global exit_flag
# exit_flag = 0

## Define a function to convert raw data into suitable format

def DueData(inputdata):   #新增的核心程序，对读取的数据进行划分，各自读到对应的数组里
    global  FrameState    #在局部修改全局变量，要进行global的定义
    global  Bytenum
    global  CheckSum
    global  a
    global  w
    global  Angle


    for data in inputdata:  #在输入的数据进行遍历

        #Python2软件版本这里需要插入 data = ord(data)
        # data = ord(data)
        # ****************************************************************************************************
        
        if FrameState==0:   #当未确定状态的时候，进入以下判断
            if data==0x55 and Bytenum==0: #0x55位于第一位时候，开始读取数据，增大bytenum
                CheckSum=data
                Bytenum=1
                continue
            elif data==0x51 and Bytenum==1:#在byte不为0 且 识别到 0x51 的时候，改变frame
                CheckSum+=data
                FrameState=1
                Bytenum=2
            elif data==0x52 and Bytenum==1: #同理
                CheckSum+=data
                FrameState=2
                Bytenum=2
            elif data==0x53 and Bytenum==1:
                CheckSum+=data
                FrameState=3
                Bytenum=2

        elif FrameState==1: # acc    #已确定数据代表加速度
            
            if Bytenum<10:            # 读取8个数据
                ACCData[Bytenum-2]=data # 从0开始
                CheckSum+=data
                Bytenum+=1
            else:
                if data == (CheckSum&0xff):  #假如校验位正确
                    # a = get_acc(ACCData)
                    acc_x,acc_y,acc_z = get_acc(ACCData)
                CheckSum=0                  #各数据归零，进行新的循环判断
                Bytenum=0
                FrameState=0

        elif FrameState==2: # gyro
            
            if Bytenum<10:
                GYROData[Bytenum-2]=data
                CheckSum+=data
                Bytenum+=1
            else:
                if data == (CheckSum&0xff):
                    # w = get_gyro(GYROData)
                    gyro_x,gyro_y,gyro_z = get_gyro(GYROData)
                CheckSum=0
                Bytenum=0
                FrameState=0

        elif FrameState==3: # angle
            
            if Bytenum<10:
                AngleData[Bytenum-2]=data
                CheckSum+=data
                Bytenum+=1
            else:
                if data == (CheckSum&0xff):
                    # Angle = get_angle(AngleData)
                    roll,pitch,yaw = get_angle(AngleData)
                    # d = a+w+Angle
                    # print("a(g):%10.3f %10.3f %10.3f w(deg/s):%10.3f %10.3f %10.3f Angle(deg):%10.3f %10.3f %10.3f"%d)
                CheckSum=0
                Bytenum=0
                FrameState=0
    return acc_x,acc_y,acc_z,roll,pitch,yaw
    # return acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z,roll,pitch,yaw
 
 
def get_acc(datahex):  
    axl = datahex[0]                                        
    axh = datahex[1]
    ayl = datahex[2]                                        
    ayh = datahex[3]
    azl = datahex[4]                                        
    azh = datahex[5]
    
    k_acc = 16.0
 
    acc_x = (axh << 8 | axl) / 32768.0 * k_acc
    acc_y = (ayh << 8 | ayl) / 32768.0 * k_acc
    acc_z = (azh << 8 | azl) / 32768.0 * k_acc

    if acc_x >= k_acc:
        acc_x -= 2 * k_acc
    if acc_y >= k_acc:
        acc_y -= 2 * k_acc
    if acc_z >= k_acc:
        acc_z-= 2 * k_acc
    
    return acc_x,acc_y,acc_z
 
 
def get_gyro(datahex):                                      
    wxl = datahex[0]                                        
    wxh = datahex[1]
    wyl = datahex[2]                                        
    wyh = datahex[3]
    wzl = datahex[4]                                        
    wzh = datahex[5]
    k_gyro = 2000.0
 
    gyro_x = (wxh << 8 | wxl) / 32768.0 * k_gyro
    gyro_y = (wyh << 8 | wyl) / 32768.0 * k_gyro
    gyro_z = (wzh << 8 | wzl) / 32768.0 * k_gyro

    if gyro_x >= k_gyro:
        gyro_x -= 2 * k_gyro
    if gyro_y >= k_gyro:
        gyro_y -= 2 * k_gyro
    if gyro_z >=k_gyro:
        gyro_z-= 2 * k_gyro

    return gyro_x,gyro_y,gyro_z
 
 
def get_angle(datahex):                                 
    rxl = datahex[0]                                        
    rxh = datahex[1]
    ryl = datahex[2]                                        
    ryh = datahex[3]
    rzl = datahex[4]                                        
    rzh = datahex[5]
    k_angle = 180.0
 
    angle_x = (rxh << 8 | rxl) / 32768.0 * k_angle
    angle_y = (ryh << 8 | ryl) / 32768.0 * k_angle
    angle_z = (rzh << 8 | rzl) / 32768.0 * k_angle

    if angle_x >= k_angle:
        angle_x -= 2 * k_angle
    if angle_y >= k_angle:
        angle_y -= 2 * k_angle
    if angle_z >=k_angle:
        angle_z-= 2 * k_angle
 
    return angle_x,angle_y,angle_z
 
 
def main():


    # use raw_input function for python 2.x or input function for python3.x

    ser = serial.Serial('/dev/ttyUSB0', 115200, bytesize=8, parity='N', stopbits=1, timeout=1)  # ser = serial.Serial('com8',115200, timeout=0.5) 
    
    if ser.is_open == True:
        print("Serial port is now connecting successfully!")
    else:
        print("Serial port is not connecting correctly! Please check your device!")


    while True:

        # get the current time stamp
        current = datetime.now()
        # now = current.strftime("%H:%M:%S")

        # get the 9-axis data of IMU module
        datahex = ser.read(33)
        # Data = DueData(datahex)
        acc_x,acc_y,acc_z,roll,pitch,yaw = DueData(datahex)
        
        print(current,acc_x,acc_y,acc_z,roll,pitch,yaw)

        # record data from IMU module into a CSV file

        with open( file_name + '.csv','a') as file:
            
            writer = csv.DictWriter(file, fieldnames=['time','acc_x','acc_y','acc_z','roll','pitch','yaw'])
            writer.writerow({'time':current,'acc_x':acc_x,'acc_y':acc_y,'acc_z':acc_z,'roll':roll,'pitch':pitch,'yaw':yaw})
            
            # # writer.writerow(['time','acc_x','acc_y','acc_z','gyro_x','gyro_y','gyro_z','roll','pitch','yaw'])
            # writer = csv.writer(file,delimiter=',',quotechar='"',quoting = csv.QUOTE_MINIMAL)
            # writer.writerow([current,acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z,roll,pitch,yaw])
            
        file.close()

      
main()

# plot_imu_data_csv(csv_file_name)

