'''
*********************************************************************************************
  *File: test_1.py
  *Project: IMU_python_reading_3.0
  *Filepath: /home/guoyucan/Downloads/IMU_Python_Reading/IMU_python_reading_3.0/test_1.py 
  *File Created: Wednesday, 22nd September 2021 7:31:58 pm
  *Author: Guo Yucan, 12032421@mail.sustech.edu.cn 
  *Last Modified: Wednesday, 22nd September 2021 7:31:59 pm
  *Modified By: Guo Yucan, 12032421@mail.sustech.edu.cn 
  *Copyright @ 2021 , BionicDL LAB, SUSTECH, Shenzhen, China 
*********************************************************************************************
'''
import numpy as np 

a = np.array([
    [1,3,4],
    [4,9,3],
    [9,0,1]
    ])

A = np.where([a >  5])

print(A)