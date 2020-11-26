#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/25 4:16 PM
# @Author: zhangzhihui.wisdom
# @File:secondarySearch.py
import sys

if __name__ == '__main__':
    print('search')
    # the first way:
    # numbers = []
    # lines = []
    # end = 'EOF'
    # print("please input multiline data (input end od file to end)")
    # for line in iter(input, end):
    #     lines.append(line)
    #
    # print(lines)
    # the second way
    strList = []
    for number in sys.stdin:
        # default split symbols are \n \t and space
        tempStr = number.split()
        strList.extend(tempStr)
        # convert a string type array to int
    strList = list(map(int, strList))
    print(strList)
    strList.sort()
    print(strList)
    print(len(strList))
    index = len(strList) // 2
    print(index)
    target = 9
    flag = False
    left = 0
    right = len(strList)
    while left <= right:
        mid = left + (right - left) >> 1
        if target == strList[mid]:
            flag = True
            break
        elif target < strList[mid]:
            mid -= 1
        else:
            mid += 1
    if flag:
        print(mid)
    else:
        print(len(strList) + 1)
