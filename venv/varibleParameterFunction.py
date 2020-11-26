#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/16 1:04 PM
# @Author: zhangzhihui.wisdom
# @File:varibleParameterFunction.py


def calc(*numbers):
    total = 0
    for n in numbers:
        total = total + n * n
    return total


if __name__ == '__main__':
    calc(1, 2, 3)
    print(calc(1, 2, 3))
