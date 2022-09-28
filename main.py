# coding=utf-8
# 此程序用于导出包括其他信息在内的eagle库
# 第一次重构

import os
import shutil

path_library = 'none'
path_images = 'none'
path_export = 0
folder_images = []
file_metadata = 'none'


# 寻找地址
def looking_for():
    global path_images, path_export, path_library
    # path_library = input("输入library文件夹路径")
    path_library = r'Z:\shu jv ku\军事.library'
    path_images = path_library + r'\\images'
    if path_images[-6:] == "images":
        pass
    else:
        print("路径错误")
    # path_export = input("请输入输出文件夹")
    path_export = r'Z:\临时文件\导出测试'


# 读取文件夹源文件并创建对应文件夹
def read_the_folder_metadata():
    path_folderdata = path_library + r'\\metadata.json'
    with open(path_folderdata, 'r',encoding='utf-8') as data:
        file_folderdata = data.read()
    filename = file_folderdata


# 读取images文件夹内信息
def read_the_imagesfolder():
    global folder_images
    folder_images = os.listdir(path_images)


# 安装文件夹分类文件
def classify_the_files():
    global file_metadata, folder_images

    num = 0
    for folder_image in folder_images:
        path_image = path_images + '\\' + folder_images[num]  # 获取子文件夹路径
        path_metadata = path_image + r"\\metadata.json"  # 获取详情文件路径
        with open(path_metadata, 'r', encoding='utf-8') as metadata:
            file_metadata = metadata.read()
        print(file_metadata.find('"folders":["'))


def main():
    looking_for()
    read_the_folder_metadata()
    read_the_imagesfolder()
    classify_the_files()


main()
