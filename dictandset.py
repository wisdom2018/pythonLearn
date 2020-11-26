#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/12 1:03 PM
# @Author: zhangzhihui.wisdom
# @File:dictandset.py

# compare list with dict ,dict has the following advantages
# the speed of find and inset extremely quick, can not become slow with the increasingly key
# need take up lots of memory, waste too much memory

# set is unique and unsort collection
# d = {'michael':95,'Bob':75,'Tracy':85}, s = set([1,3,4]),s.remove(4)


if __name__ == '__main__':
    s = set([1, 3, 4, 3])           # set can remove duplicated elements
    s.add(5)
    s.add(5)
    dic = {'michael': 95, 'Bob': 75, 'Tracy': 85}
    print(s)
    print(dic.get('michael'))       # according to the key to get the value
    print(dic.pop('Bob'))           # remove one element from dict
    print(dic)