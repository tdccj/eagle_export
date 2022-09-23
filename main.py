# coding=utf-8
# 此程序用于导出包括其他信息在内的eagle库

import os
import shutil
import time


def fenlei(type1):
    global sourec_ft, b, v
    if type1 in ('.jpg', '.png', '.jpeg', '.webp'):
        if b >= 1:
            pass
        elif v >= 1:
            pass
        else:
            print("照片")
            sourec_ft = "photo"

    elif type1 in ('.url', '.db'):
        print("网页")
        sourec_ft = "url"
        b = 1

    elif type1 in ('.mp4', '.mov', '.avi', '.mkv'):
        print("视频")
        sourec_ft = "video"
        v = 1

    else:
        if b >= 1:
            pass
        elif v >= 1:
            pass
        else:
            print("无法分类")
            sourec_ft = "other"


def dabao(a, sft, num1, selfname, export, path):
    # print(sft)
    sourec_name = a[(a.find("name") + 7):(a.find("size") - 3)]
    print(sourec_name)
    num1 = num+2

    # 写入描述文件
    data_w = open(export + "\\" + sft + "\\" + str(num1) + "_" + sourec_name + ".txt", "w")
    print(export + "\\" + sft + "\\" + str(num1) + "_" + sourec_name + ".txt")
    data_w.write('#name:'+a[(a.find('"name":"') + 8):a.find('","size"')])  # name
    data_w.write("\n")
    data_w.write('#tag:'+a[(a.find('"tags":[') + 8):a.find('],"folders"')])  # tag
    data_w.write("\n")
    data_w.write('#url:'+a[(a.find('"url":"') + 7):a.find('","annotation"')])  # url
    data_w.write("\n")
    data_w.write('#annotation:'+a[(a.find('"annotation":"') + 14):a.find('","modificationTime"')])  # annotation 注释
    data_w.write("\n")
    data_w.write("\n")
    data_w.write(a)
    data_w.close()

    # 复制源文件
    for k in selfname:
        b = path_image + "\\" + path[num] + "\\" + k
        c = export + "\\" + sft + "\\" + str(num1) + "_" + k
        print(b, c)
        shutil.copyfile(b, c)


def trymkdir(dirtype):
    try:
        os.mkdir(export + "\\" + dirtype)
    except FileExistsError:
        pass


sourec_ft = 0
a = 0
path_image = input("输入image文件夹路径")
export = input("请输入输出文件夹")
path = os.listdir(path_image)
# print(path)

# 尝试创建文件夹
trymkdir("photo")
trymkdir("video")
trymkdir("other")
trymkdir("url")

num = -1
for j in path:
    b = 0
    v = 0
    self_name = []

    path_jvbu = os.listdir(path_image + '\\' + path[num])
    # print(num)
    # print(path_jvbu)
    for i in path_jvbu:
        file_type = os.path.splitext(i)[1]

        if file_type == '.json':
            # print("json")
            # print(path_image + '\\' + path[num] + '\\' + i)
            data = open(path_image + '\\' + path[num] + '\\' + i, 'r', encoding='utf-8')
            a = data.read()
            # print("a", a)
            data.close()

        elif file_type != '.json':
            # print(file_type)
            fenlei(file_type)
            self_name.append(i)
    dabao(a, sourec_ft, num, self_name, export, path)
    num = num + 1
