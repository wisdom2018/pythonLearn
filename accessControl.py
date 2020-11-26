#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/29 9:52 AM
# @Author: zhangzhihui.wisdom
# @File:accessControl.py


# if you want to inner properties which can not access by external. we
# need add __ before the property,become the property as private variable
# in python __XX__ is special variable,this kind of variable can be accessed directly
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


if __name__ == '__main__':
    print('access control')
    tom = Student('Tom', 89)
    # tom.name()
    # print(tom.name)
    tom.get_name()
    tom.set_score('99')
    print(tom.get_name())
    print(tom.get_score())
