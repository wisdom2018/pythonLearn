#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/28 8:58 PM
# @Author: wisdom
# @File:partialFunction.py

# partial function means some parameters of the function is given,has the default value

import functools

if __name__ == '__main__':
    package_url = ""
    args = ""
    a = ""
    # not is reverse
    if not package_url:
        if not args or not a:
            print('verify')
    int2 = functools.partial(int, base=2)
    int2('1000000')
    print('partial function', int2('1000000'))
