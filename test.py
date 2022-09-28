import os
import shutil

path_library = r'Z:\shu jv ku\军事.library'
path_export = r'Z:\临时文件\导出测试'
# ——————————————————————————————————————————————————————————————————————————

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

    if kchar == '{':
        name = data[data.find('"name":', knum) + 8:data.find('"children":', knum) - 1]
        name =
        kpath = kpath + '\\' + name
        print(knum, 'yes', kpath)

        os.mkdir(kpath)

    elif kchar == '}':
        kpath = kpath[:kpath.rfind('\\')]
        print(knum, 'no', kpath)
