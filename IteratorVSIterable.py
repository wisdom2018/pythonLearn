#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/23 8:34 AM
# @Author: zhangzhihui.wisdom
# @File:IteratorVSIterable.py
from collections import Iterable, Iterator

# Collection data type: list、tuple、dict、set、str
# can use isinstance() to judge a object whether is iterable

# Iterator not only can use for loop,but also can call by next() method,
# until return StopIteration error which indicates can not return next value
if __name__ == '__main__':
    isinstance({}, Iterable)
    isinstance('abc', Iterable)
    print(isinstance({}, Iterable))
    print(isinstance('abc', Iterable))
    print(isinstance('abc', Iterator))
    # also can change a iterable object to iterator object by iter() method
    isinstance(iter('abc'), Iterator)
    print(isinstance(iter('abc'), Iterator))

    # the difference of iterator and iterable in python
    # in python, Iterator object represents a data stream, iterator object can be called by next()
    # method and return next value gradually, util has no next value and return StopIteration error.
    # we can think that this data stream is a sorted sequence, while we can not know the length of data beforehand.
    # only be next() compute next value, So the computation of Iterator is lazy computation.
    # Only calculate next value when needed

    # Iterator even can represents a infinite data stream, while list can not.
    it = iter([1, 2, 3, 4, 5])
    while True:
        try:
            x = next(it)
            print(x, "this is %d" % x)
        except StopIteration:
            break


