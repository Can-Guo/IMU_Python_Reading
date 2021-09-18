'''
*********************************************************************************************
  *File: Plot_imu_data.py
  *Project: IMU_python_reading_3.0
  *Filepath: /home/guoyucan/Downloads/IMU_Python_Reading/IMU_python_reading_3.0/Plot_imu_data.py 
  *File Created: Saturday, 18th September 2021 9:57:15 pm
  *Author: Guo Yucan, 12032421@mail.sustech.edu.cn 
  *Last Modified: Saturday, 18th September 2021 10:20:00 pm
  *Modified By: Guo Yucan, 12032421@mail.sustech.edu.cn 
  *Copyright @ 2021 , BionicDL LAB, SUSTECH, Shenzhen, China 
*********************************************************************************************
'''

import csv
import os.path

import pandas as pd
import numpy as np

def plot_imu_data_csv():

    ## Using csv module to read CSV data

    # with open('data_2021-09-18 19:08:28.439834.csv',mode='r') as csv_file:
    #     # print(csv_file)
    #     reader = csv.reader(csv_file, delimiter=',')
    #     line_counter = 0
    #     global acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z,roll,pitch,yaw

    #     for row in reader:
    #         if line_counter == 0:
    #             header = row[0]
    #             print(header)
    #             line_counter += 1
    #         else:
    #             print(row[line_counter])
    #             line_counter += 1


    ## Using pandas module to read CSV data
    data = pd.read_csv('data_2021-09-18 23:20:17.954268.csv')
    data.drop(['time'],axis=1,inplace=True) # delete specific column of data in Dataframe

    # print(type(data['time']))
    # print(data['time'].values)

    print(data.values) # convert into array format, Method 1
    print(np.array(data)) # convert into array format, Method 2


    return

plot_imu_data_csv()

