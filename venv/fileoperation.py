#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/12 4:38 PM
# @Author: zhangzhihui.wisdom
# @File:fileoperation.py
import os


# get current path
# print(os.getcwd())
# # print(os.path.abspath('.'))
# print(os.path.join('/Users/bytedance', 'test2020'))
# # print(os.path.split(os.path.abspath('.')))
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# # os.path.splitext() can get the file extension name
# # split all .py file
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# rename a file
# os.rename('test.txt', 'test.py')

# delete a file
# os.remove('test.py')

# python file relative path and absolute path
# when open one file without path, open function can search this file in current directory
# absolute path  back slash
# double back slash represents escape \\
# relative path use slash to represent /
# '.' represents the file which in directory

# program : get the current directory and all sub-directory to get contain specified string file,
# and print relative path
def listAl(current):
    # listdir means list all directories and files under current path
    for x in os.listdir(current):
        if os.path.isdir(x):
            print([x for x in os.listdir(x) if x.find('.py') == 1])

        elif os.path.isfile(x) and x.find('.py') == 1:
            print(x)


if __name__ == '__main__':
    path = input()
    print(os.getcwd())
    print(os.listdir(os.getcwd()))
    listAl(os.getcwd())

