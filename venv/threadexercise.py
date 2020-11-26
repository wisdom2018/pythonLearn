#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/16 11:25 AM
# @Author: zhangzhihui.wisdom
# @File:threadexercise.py
from threading import Thread, current_thread


def echo(num):
    print
    current_thread().name, num


def calc():
    print
    'thread %s is running' % current_thread().name
    local_num = 0
    for _ in xrange(1000):
        local_num += 1
        echo(local_num)
        print
        'thread %s is running ...' % current_thread().name


if __name__ == '__main__':
    print('thread Exercise')
    print
    'thread %s is running' % current_thread()
    threads = []
    for i in range(5):
        threads.append(Thread(target=calc))
        threads[i].start()
    for i in range(5):
        threads[i].join()

    print
    'thread %s is ended ' % current_thread().name
