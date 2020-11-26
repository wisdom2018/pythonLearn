#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/18 6:12 PM
# @Author: zhangzhihui.wisdom
# @File:recursiveImpTrim.py


def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])


if __name__ == '__main__':
    ss = input()
    print(trim(ss))
