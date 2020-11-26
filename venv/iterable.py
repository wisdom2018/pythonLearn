#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/19 11:31 AM
# @Author: zhangzhihui.wisdom
# @File:iterable.py


# Given a list or tuple,can according to the following ways to iterate them
# the fist way: use for loop
from collections import Iterable


def iterateList(student):
    for ch in student:
        print ch


if __name__ == '__main__':
    print('main function')
    s = ['1', 'b', 'c']
    dic = {'a': 1, 'b': 2, 'c': 3}
    for k, v in dic.items():
        print(k, v)
    # for key, value in dict.items() to iterate the dict to get the key and value
    # use list implement the loop from index, can use enumerate method in python
    # this method can change a  list into index-value pair,which can imp use for iterate index and value in list
    listOne = ['A', 'B', 'C']
    for i, value in enumerate(listOne):
        print(i, value)
    # isinstance method can judge object whether can iterable
    print(isinstance(dict, Iterable))
    iterateList(s)
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s for s in L1 if (isinstance(s, str))]
    print(L2)
