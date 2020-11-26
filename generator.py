#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/23 9:32 AM
# @Author: zhangzhihui.wisdom
# @File:generator.py

# the method of creating generator :
# the first method : only change the list comprehension [] to {}
# L = [x * x for x in range(10)]
# g = (x * x for x in range(10)) L is a list,while g is a generator


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print ('step 3')
    yield 5


if __name__ == '__main__':
    L = [x * x for x in range(10)]
    g = (x * x for x in range(10))
    print(L)
    print(g)
    print("generator")
    for n in g:
        print(n)
    o = odd()
    print(next(o))
    print(next(o))
# if function contains a yield, the function become a generator
# yield statement suspends function's execution and sends a value back to the caller
# but retains enough state to enable function to resume where it is left off
# when resumed, the function continues execution immediately after the last yield run.
# this allows its code to produce a series of values over time, rather than computing them at once
# and sending them back like a list

