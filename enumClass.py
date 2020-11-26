#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/2 11:49 AM
# @Author: zhangzhihui.wisdom
# @File:enumClass.py

from enum import Enum


if __name__ == '__main__':
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    dir(Month)
    for name, member in Month.iterms():
        print(name, '=>', member, ',', member.value)
    print('''enum class 
    learn
    ''')
