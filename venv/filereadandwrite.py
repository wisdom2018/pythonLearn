#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/9 6:24 PM
# @Author: zhangzhihui.wisdom
# @File:filereadandwrite.py
from io import StringIO
import os

# StringIO read and write in memory


if __name__ == '__main__':
    f = StringIO()
    f.write('Hello')
    f.write('world!')
    # getvalue method can get the str which write in memory
    print(f.getvalue())

    f1 = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f1.readline()
        if s == '':
            break
        print(s.strip())
    print([x for x in os.listdir('.') if os.path.dir(x)])
