# coding=utf-8
# 此程序用于导出包括其他信息在内的eagle库
# 第一次重构

import os
import shutil

path_library = 'none'
path_images = 'none'
path_export = 'none'
folder_images = []
file_metadata = 'none'
folders = {}  # 文件夹字典


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
    global folders

    # 打开源文件
    path_folderdata = path_library + r'\\metadata.json'
    with open(path_folderdata, 'r', encoding='utf-8') as data:
        file_folderdata = data.read()

    # 用于剔除多余的信息
    data = file_folderdata[:file_folderdata.find(',"smartFolders":')]
    data = data[data.find('{"folders":') + 11:]
    metadata = data
    print(data)

    # 用于剔除多余的信息（或许可以用replace重构
    words = [',"description":"",', ',"password":"","passwordTips":""', ',"tags":[]']
    for word in words:
        j = 0
        wnum = len(word)
        print(wnum)
        i = 0
        num = 0
        while i != -1:
            i = data.find(word, j)
            if i == -1:
                continue
            data = data[:i] + data[i + wnum:]

            # print(data[:i])
            print(i + wnum, i, wnum)
            j = i + 1
            num = num + 1
        #     print('num:' + str(num))
        #     print(i)
        print(data)

    j = 0
    k = -1
    num1 = 0
    a = []
    for i in data:
        if i == '{':
            a.append(str(num1) + '{')

        elif i == '}':
            a.append(str(num1) + '}')
        num1 = num1 + 1
    print(a)

    kpath = path_export
    name = 'none'

    for i in a:
        knum = int(i[:-1])
        kchar = i[-1:]
        # print(knum,kchar)

        # 如果是前大括号
        if kchar == '{':
            # 将name和id写入字典
            name = data[data.find('"name":', knum) + 8:data.find('"children":', knum) - 1]
            folder = data[data.find('"id":"', knum) + len('"id":"'):data.find('","name":', knum)]
            folders[folder] = {}
            folders[folder]['name'] = name

            # 前进一个文件夹
            kpath = kpath + '\\' + name
            # 将path写入字典
            folders[folder]['path'] = kpath

            print(knum, 'yes', kpath)

            # 如果文件夹已经存在，则报错error后继续执行
            try:
                os.mkdir(kpath)
            except FileExistsError:
                print("error")

        # 如果是后大括号，则退后一个文件夹
        elif kchar == '}':
            kpath = kpath[:kpath.rfind('\\')]
            print(knum, 'no', kpath)

    # 打印文件夹字典
    print(folders)


# 读取images文件夹内信息
def read_the_imagesfolder():
    global folder_images
    folder_images = os.listdir(path_images)


# 安装文件夹分类文件
def classify_the_files():
    global file_metadata, folder_images

    num = 0
    filenum = 1

    for folder_image in folder_images:

        # 读取所在文件夹
        path_image = path_images + '\\' + folder_images[num]  # 获取子文件夹路径
        path_metadata = path_image + r"\\metadata.json"  # 获取详情文件路径
        with open(path_metadata, 'r', encoding='utf-8') as metadata:
            file_metadata = metadata.read()
        image_folder_id = file_metadata[
                          file_metadata.find('"folders":[') + len('"folders":['):file_metadata.find('],"isDeleted":')]
        num = num + 1

        # 删除多余的引号
        image_folder_id = image_folder_id.replace('"', '')

        # 处理单个文件多文件夹
        i = 0
        folder_image = []

        while i != -1:
            i = image_folder_id.find(',', i + 1)
            # print(image_folder_id)
            # print(i)

            # 当没有逗号时直接复制
            if i != -1:
                folder_image.append(image_folder_id[:i])
            else:
                folder_image.append(image_folder_id)

            image_folder_id = image_folder_id[i + 1:]
            print(image_folder_id)

        for folder_id in folder_image:

            # 解决意外出现的空值
            if folder_id == '':
                continue

            path_export_image = folders[folder_id]['path']
            print(path_export_image)
            image_folder = os.listdir(path_image)

            for file in image_folder:
                if file == 'metadata.json':
                    continue
                file = str(filenum) + '-' + file
                filename = os.path.splitext(file)[0]
                print(filename)
                path1 = path_image + '\\' + file
                path2 = path_export_image + '\\' + file
                print(path1,path2)
                shutil.copy(path1,path2)
            file = image_folder[image_folder.index('metadata.json')]
            file = str(filenum) + '-' + file
            shutil.copy(path_image + '\\' + file, path_export_image + '\\' + file)

        filenum = filenum + 1


def main():
    looking_for()
    read_the_folder_metadata()
    read_the_imagesfolder()
    classify_the_files()


main()
