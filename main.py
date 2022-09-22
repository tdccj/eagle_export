# coding=utf-8
# 此程序用于导出包括其他信息在内的eagle库

import os

path = input("输入image文件夹路径")
path = os.listdir(path)
print(path)
num = 0
for i in path:
    data = os.path.splitext(path[num])
    num = num + 1
    # print(data)
    # print(data[1])
    data1 = data[1]
    if data1 == '.jpg' or '.png' or '.jpeg' or '.webp':
        print("照片")
