#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/16 5:33 PM
# @Author: zhangzhihui.wisdom
# @File:regularExpression.py
import re

if __name__ == '__main__':
    print('identify the email')
    email = 'someone@gmail.com'
    print(re.match(r'^([a-zA-Z\.0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z]{3}$', email))

    if re.match(r'^([a-zA-Z\.0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z]{3}$', email):
        print(True)
    else:
        print(False)
