#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/29 9:42 AM
# @Author: zhangzhihui.wisdom
# @File:class.py


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


if __name__ == '__main__':
    print('class character')
    tom = Student('Tom', 89)
    tom.print_score()
