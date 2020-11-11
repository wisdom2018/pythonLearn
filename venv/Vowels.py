#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/11/11 8:08 PM
# @Author: zhangzhihui.wisdom
# @File:Vowels.py


def reverseVowels(strs):
    # Vowels character is a e i o u
    dic = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    left = 0
    right = len(strs) - 1
    s_ = list(strs)
    while left < right:
        if s_[left] in dic and s_[right] in dic:
            s_[left], s_[right] = s_[right], s_[left]
            left += 1
            right -= 1
        if s_[left] not in dic:
            left += 1
        if s_[right] not in dic:
            right -= 1
    return ''.join(s_)


if __name__ == '__main__':
    str1 = input()
    str2 = reverseVowels(str1)
    print(str2)

