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

# import csv
# import os.path

from datetime import datetime
from numpy.core.records import record
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_imu_data_csv(csvfilename=None):

    ## Method 1 : Using csv module to read CSV data generated

    ## Method 2 : Using pandas module to read CSV data generated
    
    data_frame = pd.read_csv(csvfilename)
    data_frame.drop(['time'],axis=1,inplace=True) # delete specific column of data in Dataframe, time

    # print(data.values) # convert into array format, Method 1
    data = np.array(data_frame) # convert into array format, Method 2

    acc_x_record = data[:,0]
    acc_y_record = data[:,1]
    acc_z_record = data[:,2]

    roll_record  = data[:,3]
    pitch_record = data[:,4]
    yaw_record   = data[:,5]

    time_sequence = np.linspace(0,len(roll_record),len(roll_record))

    plt.figure()

    plot=[None]*6
    plot[0] = plt.subplot(321)
    plot[1] = plt.subplot(322)
    plot[2] = plt.subplot(323)
    plot[3] = plt.subplot(324)
    plot[4] = plt.subplot(325)
    plot[5] = plt.subplot(326)
    
    xlabel = 'time frame'
    ylabel = ['roll data','accerelation of x axis', 'pitch data', 'accerelation of y axis', 'yaw data','accerelation of z axis']
    legend = ['roll angle','x-axis accerelation', 'pitch angle', 'y-axis accerelation', 'yaw angle',  'z-axis accerelation']
    data_record = [roll_record,acc_x_record,pitch_record,acc_y_record,yaw_record,acc_z_record]
    color = ['r-.','c-','g-o','y-','b-*','m-']

    for i in range(6):

      plot[i].plot(time_sequence, data_record[i], color[i], label = legend[i])
      plot[i].set_xlabel(xlabel)
      plot[i].set_ylabel(ylabel[i]) 

    for i in range(6):

      plot[i].legend()
      plot[i].grid()

    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    current = datetime.now()
    fig_name = './' + str(current) + '.png'
    res = plt.savefig(fig_name,dpi=800)

    plt.show()

    return

# call the function to plot imu data from csv

plot_imu_data_csv(csvfilename='data_2021-09-19 10:49:14.390817.csv')

