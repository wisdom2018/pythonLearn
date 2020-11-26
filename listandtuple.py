#!/usr/bin/python
# -*- coding: utf-8 -*-
# import os,sys
"""
user indentity verify

"""


# list is can changed,support insert and append as well as pop
# pop any position element and insert any position
# insert(index,element)
# pop(i)
# replace any position element : list[index] = element
# list can have different type element and also support nested list,s = ['python', 'java', ['asp', 'php'], 'scheme']
def verify():
    username = input('请输入用户名: ')
    password = input('请输入口令: ')

    if username == 'admin' and password == '123456':
        print('身份验证成功！')
    else:
        print('身份验证失败')


if __name__ == '__main__':
    verify()
    # when the tuple just contain 1 element，need ，to distinguish the () of mathematics
    # can not modify tuple
    t = (1,)
    print(t)
    tt = ('a', 'b', ['A', 'B'])
    tt[2][0] = 'X'
    tt[2][1] = 'Y'
    print(tt)
    # From superficially,the elements of tuple definitely changed,actually the elements of tuple has't changed
    # while the element of list has been changed
    # tuple is constant, meaning the tuple which refer to the address of variable is constant ,not the value
    # once the tuple is initialized, the value of tuple can not change

