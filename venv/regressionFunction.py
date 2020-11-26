#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/16 1:29 PM
# @Author: zhangzhihui.wisdom
# @File:regressionFunction.py


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    fact(2)
    print(fact(2))

# using the recursive,please attention the stack overflow
