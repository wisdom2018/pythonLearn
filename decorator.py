#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/25 10:09 AM
# @Author: zhangzhihui.wisdom
# @File:decorator.py


# during the function running, to add the feature dynamically,called decorator
# introduce the *args and **kwargs
# in python,we can pass a variable number of arguments to a function using special symbols.
# there are two special symbols
# 1.*args(None keyword Arguments)
# 2.**kwargs(keyword Arguments)
# we use *args and **kw as an arguments when we are unsure about the number of arguments to pass in the function
# In the function, we should use an asterisk * before the parameter name to pass variable length arguments.
# The arguments are passed as a tuple and these passed arguments
# make tuple inside the function with same name as the parameter excluding asterisk *
def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper()


@log
def now():
    print('2020-7-28')


# using *args to pass the variable length arguments to the function
def adder(*num):
    total = 0
    for n in num:
        total = total + n
    print("Total:", total)


# python passes variable length non keyword argument to function using *args
# but we cannot use this to pass keyword argument.
# for solving this problem. python can use **kwargs,
# it allows us to pass the variable length of keyword arguments to the function
# in the function , we use the double asterisk(**) before the parameter name to
# denote this type of argument
# this arguments are passed as a dictionary and these arguments make a dictionary inside
# function with the same as the parameter excluding double asterisk
def intro(**data):
    print("\n Data type of arguments:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


if __name__ == '__main__':
    adder(3, 4)
    adder(3, 4, 5, 6)
    intro(Firstname="lucky", Lastname="hello", Age=22, phone=123232)
