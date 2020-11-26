#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/19 10:12 PM
# @Author: zhangzhihui.wisdom
# @File:listComprehension.py


# list comprehensions
if __name__ == '__main__':
    list(range(1, 10))
    print(list(range(1, 10, 2)))
    print('Hello world')
    result = [s * s for s in range(1, 10)]
    print(result)
    # if behind for , is a select from list
    resultOne = [s * s for s in range(1, 10) if s % 2 == 0]
    print(resultOne)
    # if before for , is a result,must be a value
    resultTwo = [x if x % 2 == 0 else -x for x in range(1, 11)]
    print(resultTwo)
    # isinstance(s,str) is built-in function for python, to judge a variable whether is a string type
