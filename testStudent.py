#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/5 8:17 PM
# @Author: zhangzhihui.wisdom
# @File:testStudent.py

from Student import Student
import unittest


class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Mon', 80)
        s2 = Student('Tom', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Baer', 60)
        s2 = Student('Tus', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


if __name__ == '__main__':

    unittest.main()
