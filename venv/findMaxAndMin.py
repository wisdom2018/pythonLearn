#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/19 12:21 PM
# @Author: zhangzhihui.wisdom
# @File:findMaxAndMin.py
# using iterable implement to find max value and min value of list, and return type is tuple


def findMax(number):
    if not number:
        return [None, None]
    else:
        min_value = number[0]
        max_value = number[0]
        for i in number:
            if i < min_value:
                min_value = i
            elif i > max_value:
                max_value = i
    return [min_value, max_value]


if __name__ == '__main__':
    listOne = [2, 3, 6, 9, 1, 4]
    print(listOne[:1], listOne[-1:])
    findMax(listOne)
    print(findMax(listOne))
