### NOTE:

For Linux, you should make sure the USB port in your /dev dir.
#### 1. Before you run the data reading, you should change the pemission of the USB port device:
#### 2. $: sudo chmod 666 /dev/ttyUSB*      // (you may change '*' into a int number 0 or 1 or ...)
#### 3. You can list the availiable USB device by running the <listcom.py>

For Windows, you should make sure the COM port in your Device Manager.
#### 1. You can list the availiable USB device by running the <listcom.py>

### File Tree:

#### -IMU_python_reading_3.0
    - listcom.py  ->  list all the avaiable COM or USB devices, help you to choose the correct serial port.
    - WitSensor_copy.py  --> reading IMU data, recording data into CSV file
    - WitSensor.py --> original code by https://www.wit-motion.com/

#### -IMU_Python_1.0_2.0
    - WitSensor.py --> modified based on the original code from https://www.wit-motion.com/
    - test_read_mu_2.py --> Test the <WitSensor.py> script


version : 3.0.0

1. author : Can-Guo, 12032421@mail.sustech.edu.cn
2. Date : 2021.09.18
3. Modification 1: revision for data recording into a CSV file
4. Modification 2: add a module to plot the imu data from the resultant CSV file we got before

version : 2.0.0
1. intempt to implement as a function which could feedback data for N-times (mean value) -- IMU
2. author : Can-Guo, 12032421@mail.sustech.edu.cn
3. Date : 2021.07.14


**********************************************************************************************************
ubuntu -->



1. Connect the JY61 with a USB-TTL adaptor, the connection flow would be

    [PC] <--> [USB-TTL Adaptor] <--> [JY61 sensor]
    
2. open a terminal, type
pip3 install pyserial
3. run the python script <test_read_imu_2.py> to read the data from JY61
4. Noted that: the Module <Witsensor.py> should in the same folder with <test_read_imu_2.py>.


version : 1.0.0 

**********************************************************************************************************
Windows -->


1. 运行前需先安装pyserial，用WIN+R调出运行框，输入CMD，进入命令行，输入pip install pyserial更新一下函数库.
2. 教程地址：https://blog.csdn.net/Fred_1986/article/details/114415548
3. 软件下载地址：https://download.csdn.net/download/Fred_1986/15602449
4. 视频教程：https://www.bilibili.com/video/BV1bV411v7Bm/


