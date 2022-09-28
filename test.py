import os
import shutil

path_folderdata = r'Z:\临时文件\测试.library' + r'\\metadata.json'
with open(path_folderdata, 'r') as data:
    file_folderdata = data.read()

# 用于剔除多余的信息
data = file_folderdata[:file_folderdata.find(',"smartFolders":')]
data = data[data.find('{"folders":') + 11:]
metadata = data
print(data)


j = 0
words = ['"description":"",','"password":"","passwordTips":""','"tags":[],sswordTips":""']
for word in words:
    # print(word)
    i = 0
    num = 0
    while i != -1:
        i = data.find(word, j)
        data = data[:i] + data[i + 17:]
        print(data[:i])
        j = i + 1
        num = num + 1
    #     print('num:' + str(num))
    #     print(i)
    print(data)

#
#
# j = 0
# k = -1
# num = 0
# a = []
# for i in data:
#     if i == '{':
#         a.append(str(num)+'{')
#
#
#     elif i == '}':
#         a.append(str(num)+'}')
#     num = num+1
# print(a)
