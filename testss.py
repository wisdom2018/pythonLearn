#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/5 7:50 PM
# @Author: zhangzhihui.wisdom
# @Filfrom mydict import Dict

import unittest
from mydict import Dict


class TestDict(unittest.TestCase):

    def test__init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'Value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    # python with key:
    # with expression:
    # with EXPR as VAR
    #  BLOCK
    # EXPR can be any expression,as VAR is optional
    # with equal try/finally
    # python provide with syntax，to simplify clean operation after resource operation，
    # which is the replacement of try/finally，implementation principle is context manager

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()
