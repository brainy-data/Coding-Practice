# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:19:52 2020

@author: Brian
"""

#剑指 Offer 40- 最小的k个数
#JZoffer 10a. return the smallest k number from a list
#Example
#Input: arr = [3,2,1], k = 2
#Output: [1,2] or [2,1]
#Input: arr = [0,1,2,1], k = 1
#Output:[0]

arr = [0, 1, 2, 1]
k = 2
#Method 1

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        return arr[:k]
#testing  
solution=Solution()
output=solution.getLeastNumbers(arr, k)
print(output)

#Method 1.1 - require heapq

import heapq

class Solution(object):
    def getLeastNumbers(self, arr, k):
        return heapq.nsmallest(k, arr)

#testing  
solution=Solution()
output=solution.getLeastNumbers(arr, k)
print(output)

#Other methods in Leetcode, to study later
