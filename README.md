### 1. Configuration for Linux & Windows

#### For Linux, you should make sure the USB port of the IMU in your /dev dir.

##### 	a. Before you run the data reading script, you should change the pemission of the USB port device by the following command 

``` shell
sudo chmod 666 /dev/ttyUSB*      // (you may change '*' into a int number 0,1,2 ...)
```

##### 	b. You can list the availiable USB device by running the <listcom.py>

```shell
python3 listcom.py
```



#### For Windows, you should make sure the COM port of the IMU in your Device Manager.

##### 	a. You can also list the availiable USB device by running the <listcom.py> at your IDE or command window.




### 2. File Tree

```
 📂IMU_Python_1.0_2.0
  ┣ 📜WitSensor.py
  ┗ 📜test_read_imu_2.py
 📂IMU_python_reading_3.0
  ┣ 📜IMU_Plotting_CSV.py
  ┣ 📜IMU_Reading_3.0.py
  ┣ 📜IMU_Reading_Recording_Plotting.py
  ┗ 📜WitSensor.py
 📂csv
  ┣ 📜data_2021-09-22 20:21:33.192971_forward_ok_1.csv
  ┣ 📜data_2021-09-22 20:26:45.136785_forward_ok_2.csv
  ┣ 📜data_2021-09-22 20:32:37.902621_forward_ok_3.csv
  ┣ 📜data_2021-09-22 20:50:04.713883_lateral_ok_1.csv
  ┣ 📜data_2021-09-22 20:54:37.761909_lateral_ok_2.csv
  ┣ 📜data_2021-09-22 21:07:02.023691_lateral_ok_3.csv
  ┣ 📜data_2021-09-22 21:14:16.327567_turning_ok_1.csv
  ┣ 📜data_2021-09-22 21:18:19.296148_turning_ok_2.csv
  ┣ 📜data_2021-09-22 21:23:24.251881_turning_ok_3.csv
  ┗ 📜data_2021-09-28 21:54:43.609238_turning_ok_4.csv
 📂fig
  ┣ 📜FORWARD_FIG.png
  ┣ 📜LATERAL_FIG.png
  ┣ 📜TURNING_FIG_1.png
  ┣ 📜TURNING_FIG_2.png
  ┣ 📜forward_fig_1.png
  ┣ 📜forward_fig_2.png
  ┣ 📜forward_figure_ok_1.png
  ┣ 📜imu_data_20210928.zip
  ┣ 📜imu_data_20211005.zip
  ┣ 📜imu_data_figure_20210927.zip
  ┣ 📜lateral_fig_1.png
  ┣ 📜lateral_fig_2.png
  ┣ 📜lateral_figure_ok_1.png
  ┣ 📜turning_fig_1.png
  ┣ 📜turning_fig_2.png
  ┣ 📜turning_figure_ok_1.png
  ┗ 📜turning_figure_ok_2.png
📜.gitignore
📜LICENSE
📜README.md
📜listcom.py

```



### 3. Note for windows & Linux

#### 		< Linux>

1. ##### Connect the JY61 with a USB-TTL adaptor, the connection flow would be

    [PC]   <==>   [USB-TTL Adaptor]   <==>   [JY61 sensor]
    
2. ##### open a terminal, type

      ```shell
      pip3 install pyserial
      ```

3. ##### run the python script <test_read_imu_2.py> to test the imu sensor. If you get IMU data stream at your terminal, then the sensor is good.

    ```shell
    python3 test_read_imu_2.py
    ```

4. ##### Note that: the Module <Witsensor.py> should in the same folder with <test_read_imu_2.py>.




#### 		< Windows>


1. ##### 运行前需先安装pyserial，用WIN+R调出运行框，输入cmd，进入命令行，输入pip install pyserial更新一下函数库.

   ```powershell
   pip install pyserial
   ```

2. ##### 官方教程地址：https://blog.csdn.net/Fred_1986/article/details/114415548

3. ##### Python下载地址：https://www.python.org/downloads/

4. ##### 官方视频教程：https://www.bilibili.com/video/BV1bV411v7Bm/



### 4. Version Record

​	version : 3.0.0

1. author : Can-Guo, 12032421@mail.sustech.edu.cn
2. Date : 2021.09.18
3. Modification 1: revision for data recording into a CSV file
4. Modification 2: add a module to plot the imu data from the resultant CSV file we got before



​	version : 2.0.0

1. intempt to implement as a function which could feedback data for N-times (mean value) -- IMU
2. author : Can-Guo, 12032421@mail.sustech.edu.cn
3. Date : 2021.07.14



​	version : 1.0.0 

1. initial implement
