#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/2 12:34 PM
# @Author: zhangzhihui.wisdom
# @File:errorHandle.py


# error的传递是不断向上的
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


if __name__ == '__main__':
    main()
    print('try.....')
    try:
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print ('except:', e)
    finally:
        print ('finally ...')
    print('END')
