
version : 3.0.0

1. author : Can-Guo, 12032421@mail.sustech.edu.cn
2. Date : 2021.09.18
3. revision for data recording into a csv file


version : 2.0.0
1. intempt to implement as a function which could feedback data for N-times (mean value) -- IMU
2. author : Can-Guo, 12032421@mail.sustech.edu.cn
3. Date : 2021.07.14


###############
ubuntu -->
###############


1. Connect the JY61 with a USB-TTL adaptor, the connection flow would be

    [PC] <--> [USB-TTL Adaptor] <--> [JY61 sensor]
    
2. open a terminal, type
pip3 install pyserial
3. run the python script <test_read_imu_2.py> to read the data from JY61
4. Noted that: the Module <Witsensor.py> should in the same folder with <test_read_imu_2.py>.


version : 1.0.0 

###############
Windows -->
###############

1. 运行前需先安装pyserial，用WIN+R调出运行框，输入CMD，进入命令行，输入pip install pyserial更新一下函数库.
2. 教程地址：https://blog.csdn.net/Fred_1986/article/details/114415548
3. 软件下载地址：https://download.csdn.net/download/Fred_1986/15602449
4. 视频教程：https://www.bilibili.com/video/BV1bV411v7Bm/


