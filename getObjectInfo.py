#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/29 10:14 AM
# @Author: zhangzhihui.wisdom
# @File:getObjectInfo.py

# to judge the type of object
# type() and also the type return the class type
# isinstance() to judge an object whether is a type
# dir() to get one object all methods and properties
# setattr()
if __name__ == '__main__':
    type(123)
    type(abs)
    isinstance('a', str)
    isinstance(1, int)
    isinstance([1, 2, 3], (list, tuple))
    dir('ABC')
