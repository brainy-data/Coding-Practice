# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:51:50 2020

@author: Brian
"""

#剑指 Offer 17. 打印从1到最大的n位数
#JZoffer 17. listing number from 1 to largest possible n-digit number
#Example
#Input:  1
#Output: [1,2,3,4,5,6,7,8,9]
# Input 2
#Output [1,2,....,98,99]

n=1

#Method1
class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #note: when using range, it is (x,y) not (x:y)
        return list(range(1,10**n))

#testing part
solution = Solution()
output = solution.printNumbers(n)
print(output)

#Method1.1 - logical rationale not chnaged
class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #note: when using range, it is (x,y) not (x:y)
        return [i for i in range (1,10**n)]

#testing part
solution = Solution()
output = solution.printNumbers(n)
print(output)