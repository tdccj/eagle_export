# coding=utf-8
# 此程序用于导出包括其他信息在内的eagle库

import os
import time


def fenlei(type1):
    global sourec_ft
    if type1 in ('.jpg', '.png', '.jpeg', '.webp'):
        print("照片")
        sourec_ft = "photo"

    elif type1 == '.url':
        print("网页")
        sourec_ft = "url"
    else:
        print("无法分类")
        sourec_ft = "other"

def dabao(a):


    data_w = open(export + "\\" + os.path.splitext(path_jvbu[0])[0] + ".txt", "w")  # 此处并不能保证不出错
    data_w.write(a)
    data_w.close()


path_image = r"Z:\shu jv ku\军事.library\images"  # input("输入image文件夹路径")
export = r"Z:\临时文件\59\ZTZ-59"  # input("请输入输出文件夹")
path = os.listdir(path_image)
print(path)
num = -1
for j in path:
    path_jvbu = os.listdir(path_image + '\\' + path[num])
    num = num + 1
    # print(path_jvbu)
    for i in path_jvbu:
        # print(i)
        file_type = os.path.splitext(i)[1]

        if file_type == '.json':
            print(path_image + '\\' + path[num] + '\\' + i)
            data = open(path_image + '\\' + path[num] + '\\' + i, 'r', encoding='utf-8')
            a = data.read()
            print("a", a)
            data.close()


        elif file_type != '.json':
            print(file_type)
            fenlei(file_type)
