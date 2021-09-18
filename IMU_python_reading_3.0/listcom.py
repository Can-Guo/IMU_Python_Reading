'''
Date: 2021-08-04 22:49:53
LastEditors: Guo Yuqin,12032421@mail.sustech.edu.cn
LastEditTime: 2021-09-18 12:46:46
FilePath: \Python\listcom.py
'''

import serial #导入模块
 
import serial.tools.list_ports
port_list = list(serial.tools.list_ports.comports())
print(port_list)

if len(port_list) == 0:
    print('无可用串口')
else:
    for i in range(0,len(port_list)):
        print(port_list[i])