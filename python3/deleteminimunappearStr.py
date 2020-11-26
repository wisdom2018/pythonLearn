#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/24 5:35 PM
# @Author: zhangzhihui.wisdom
# @File:deleteminimunappearStr.py
if __name__ == '__main__':
    st = input()
    dic = {}
for ch in st:
    if ch in dic:
        dic[ch] = dic[ch] + 1
    else:
        dic[ch] = 1

for i in dic:
    if dic[i] == min(dic.values()):
        st = st.replace(i, "")
print(st)
