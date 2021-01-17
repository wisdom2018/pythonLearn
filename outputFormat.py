#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/17 8:05 PM
# @Author: wisdom
# @File:outputFormat.py


if __name__ == '__main__':
    print('format exercise')
    # method one : %
    print('hello, %s,you have %s' % ('Miachel', 1000))

    # method two :format()方法
    print('hello,{},成绩提高了{}%'.format('小明', 17.23))

    # method three: f-string
    r = 2.5
    s = 3.14 * r ** 2
    print(f'the area of the circle with radius {r} is {s:.2f}')
