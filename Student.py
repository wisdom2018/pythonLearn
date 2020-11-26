#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/5 8:14 PM
# @Author: zhangzhihui.wisdom
# @File:Student.py


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'


