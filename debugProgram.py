#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/2 4:33 PM
# @Author: zhangzhihui.wisdom
# @File:debugProgram.py
import logging
import os

logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('1')


if __name__ == '__main__':
    print('debug the program')
    main()
    # according to print statement
    # assert statement
    # if the assertion is failure, the statement of assertion will pop AssertionError
    # the third way is according to logging
    # logging has some advantages: permit you assignment the level of the debug info
    m = '1'
    r = int(m)
    logging.info('n = %d' % r)
    print(10 / r)
    print(os.path.dirname(__file__))
