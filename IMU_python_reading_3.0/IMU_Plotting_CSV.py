'''
*********************************************************************************************
  *File: IMU_Plotting_CSV.py
  *Project: IMU_python_reading_3.0
  *Filepath: /home/guoyucan/Downloads/IMU_Python_Reading/IMU_python_reading_3.0/IMU_Plotting_CSV.py 
  *File Created: Saturday, 18th September 2021 9:57:15 pm
  *Author: Guo Yucan, 12032421@mail.sustech.edu.cn 
  *Last Modified: Saturday, 18th September 2021 10:20:00 pm
  *Modified By: Guo Yucan, 12032421@mail.sustech.edu.cn 
  *Copyright @ 2021 , BionicDL LAB, SUSTECH, Shenzhen, China 
*********************************************************************************************
'''

# import csv
# import os.path

from datetime import datetime, time
from numpy.core.fromnumeric import ptp
# from numpy.core.records import record
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_imu_data_csv(csvfilename=None, flag=0, a = 0, b = 0):

    ## Method 1 : Using csv module to read CSV data generated

    ## Method 2 : Using pandas module to read CSV data generated (selected method)
    
    data_frame = pd.read_csv(csvfilename)
    frame_number = len(data_frame['time'])
    
    data_frame.drop(['time'],axis=1,inplace=True) # delete specific column of data in Dataframe, time
    
    unusual_data = data_frame[np.abs(data_frame.roll) >= 30.0].index.tolist()
    

    # print(data.values) # convert into array format, Method 1
    data = np.array(data_frame) # convert into array format, Method 2 (selected method)
    
    # remove the unusual data which is due to the error or exception of IMU

    data = np.delete(data,unusual_data,axis=0)

    leng = data.shape[0]
    print(leng)

    ## select the specific time frame zone

    data = np.delete(data, np.s_[0:a],axis=0)
    data = np.delete(data, np.s_[b:],axis=0)
    

    leng_new = data.shape[0]

    print(leng_new)

 
    acc_x_record = data[:,0]
    acc_y_record = data[:,1]
    acc_z_record = data[:,2]

    roll_record  = data[0:b-a,3]
    pitch_record = data[0:b-a,4]
    yaw_record   = data[0:b-a,5]
    

    ###
    ## for turning, roll angle error abjustment
    error_delta = roll_record[418]-roll_record[417]
    print(error_delta)

    roll_record[418:500] = roll_record[418:500] - error_delta
    # print(roll_record[400:500])
    ###

    frame_size = b-a
    frequency = 100.0
    time_sequence = np.linspace(0,frame_size/frequency,frame_size)


    # create a figure object
    plt.figure(figsize=(20,10))

    # flag == 0 , go forward data plotting or go laterward data plotting 
    if flag == 0:
      plt.plot(time_sequence,roll_record,'r--', label = 'roll angle')
      plt.plot(time_sequence,pitch_record,'g-', label = 'pitch angle')
      # plt.plot(time_sequence,yaw_record,'b', label = 'yaw angle (degree)')
      plt.ylim([-10,10])

    # flag == 1 , go on a circle trajectory
    elif flag == 1:
      # plt.plot(time_sequence,roll_record,'r--', label = 'roll angle')
      # plt.plot(time_sequence,pitch_record,'g-.', label = 'pitch angle')
      plt.plot(time_sequence,yaw_record,'b-.', label = 'yaw angle')
      plt.ylim([-10,190])

    plt.xlim([0.0,5.0])
    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)

    plt.ylabel('angle (deg)',fontsize=35)
    plt.xlabel('time (sec)',fontsize=35)
    # plt.xlim([0,frame_size])

    plt.legend(fontsize=35)
    plt.grid()


    ##################################################
    # plot=[None]*6
    # plot[0] = plt.subplot(321)
    # plot[1] = plt.subplot(322)
    # plot[2] = plt.subplot(323)
    # plot[3] = plt.subplot(324)
    # plot[4] = plt.subplot(325)
    # plot[5] = plt.subplot(326)

    # xlabel = 'time frame'
    # ylabel = ['roll data','accerelation of x axis', 'pitch data', 'accerelation of y axis', 'yaw data','accerelation of z axis']
    # legend = ['roll angle','x-axis accerelation', 'pitch angle', 'y-axis accerelation', 'yaw angle',  'z-axis accerelation']
    # data_record = [roll_record,acc_x_record,pitch_record,acc_y_record,yaw_record,acc_z_record]
    # color = ['r--','c-','g--','y-','b--','m-']

    # for i in range(6):

    #   plot[i].plot(time_sequence, data_record[i], color[i], label = legend[i])
    #   plot[i].set_xlabel(xlabel)
    #   plot[i].set_ylabel(ylabel[i]) 

    # for i in range(6):

    #   plot[i].legend()
    #   plot[i].grid() 

    ## Resize the figure windows

    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()
    
    ##################################################


    current = datetime.now()
    fig_name = './fig/' + str(current) + '.png'
    res = plt.savefig(fig_name,dpi=600)

    plt.show()

    return 

# Test the module with callback of the plot function plot_imu_data_csv
# call the function to plot imu data from CSV

plot_imu_data_csv(csvfilename='data_2021-09-28 21:54:43.609238_turning_ok_4.csv', flag = 1, a = 600, b = 1100 )

