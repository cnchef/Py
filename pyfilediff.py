#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/16 20:28
# @Author  : chenf
# @Site    : 
# @File    : pyfilediff.py
# @Software: PyCharm

import difflib
import win32api


files = "C:\\Users\\Administrator\\Desktop\\001.txt"
files1 = "C:\\Users\\Administrator\\Desktop\\002.txt"

'''
f = open(files,"r")
print(f.read())
f.close()
'''
'''
#设置文件传参变量
files_path = sys.argv[1]
files1_path = sys.argv[2]

with open(files_path,'r') as f:
    print(files_path)
    files_list = f.readlines()
with open(files1_path,'r') as f:
    files1_list = f.readlines()
'''


#方法一，将对比结果写入HTML文件
with open(files,'r') as f:
    files_list = f.readlines()
with open(files1,'r') as f:
    files1_list = f.readlines()

diff = difflib.HtmlDiff()
html = diff.make_file(files_list,files1_list)

with open('C:\\Users\\Administrator\\Desktop\\diff.html','w',encoding='utf8') as f:
    f.write(html)

#前台打开文件
win32api.ShellExecute(0, 'open', 'C:\\Users\\Administrator\\Desktop\\diff.html', '', '', 1)



# #方法二，对比结果输出到屏幕
# with open(files,'r') as f:
#     files_list = f.readlines()
# with open(files1,'r') as f:
#     files1_list = f.readlines()
#
# diff = difflib.Differ()
# content = diff.compare(files_list,files1_list)
# for i in content:
#     print(i)

