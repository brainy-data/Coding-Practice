# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:33:42 2021

@author: Brian
"""
#剑指 Offer  65. 不用加减乘除做加法
#JZoffer  65. do summation without arithmetric operators
#Example
#Input: a = 1, b = 1
#Output: 2

#To study later - involves concept of Bitwise operation

class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

a = 1
b = 1

#testing part
output = Solution().add(a,b)
print(output)
