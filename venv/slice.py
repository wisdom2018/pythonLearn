#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/18 3:45 PM
# @Author: zhangzhihui.wisdom
# @File:slice.py

# get some elements of list and tuple,for example,get fore-three elements

if __name__ == '__main__':
    listOne = ['Mike', 'Jack', 'Mine', 'G']
    out = [listOne[0], listOne[1], listOne[2]]
    print(out)
    # using slice is very flexible
    print(listOne[0:3])
    # using listOne[-1] represent the last one element
    print(listOne[-1])
    # using slice can get element with constant break
    print(listOne[0:3:2])

    # string also can see a kind of list

    print('ABCDEFG'[0:3])
    print('ABCDEFG'[::2])
