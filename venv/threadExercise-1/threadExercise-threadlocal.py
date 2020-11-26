#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/16 2:35 PM
# @Author: zhangzhihui.wisdom
# @File:threadExercise-threadlocal.py

import threading

global_num = 0
xrange = range


def thread_cal():
    global global_num
    for i in xrange(1000):
        global_num += 1

    # Get 10 threads,run them and wait them all finished
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=thread_cal))
        threads[i].start()
    for i in range(10):
        threads[i].join()
    print
    global_num


if __name__ == '__main__':
    thread_cal()
    print('global variable')
