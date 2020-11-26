#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/12 11:45 AM
# @Author: zhangzhihui.wisdom
# @File:conditionidentify.py


def cal(weight, height):
    bmi = weight / (height * height)
    if bmi < 18.5:
        result = 'over light'
    elif 18.5 <= bmi < 25:
        result = 'normal'
    elif 28 <= bmi < 32:
        result = 'fat'
    else:
        result = 'fat seriously'
    print(result)

# elif is the abbreviation of elseif
    if __name__ == '__main__':
        print('main')
    # input the return value is string,must switch to integer that can use comparing digit value
    weight = input('weight: ')
    height = input('height：')
    weightInteger = int(weight)
    heightInteger = int(height)
    cal(weightInteger, heightInteger)
