# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:20:55 2020

@author: Brian
"""

#剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
#JZoffer 21. Rearrange list of intergers so that odd numbers followed by even numbers
#Example 1
#Input:  [1,2,3,4]
#Output: both [3,1,2,4] or [1,3,2,4] are acceptable

nums = [1,2,3,4,5,6]

#Method 1: initiate two list and then join them together
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd = []
        even =[]
        for i in nums:
            if i % 2 == 0:
               even.append(i)
            else:
                odd.append(i)
        return odd + even
#Testing part
solution = Solution()
output=solution.exchange(nums)
print(output)

#Method 2 - very time-consuming
class Solution(object):
    def exchange(self, nums):
        res = []
        for i in nums:
            if i % 2 == 0:
               res.append(i)
            else:
                res = [i] + res
        return res
#Testing part
solution = Solution()
output=solution.exchange(nums)
print(output)

#Method 3: less time-consuming than method 2, but still time-consuming
class Solution(object):
    def exchange(self, nums):
        res = []
        for i in nums:
            if i % 2 == 0:
               res.append(i)
            else:
                res.insert(0,i)
        return res
#Testing part
solution = Solution()
output=solution.exchange(nums)
print(output)
    
#Method 4: use external library (deque) and hence get appendleft method
#same speed as method 1
from collections import deque

class Solution(object):
    def exchange(self, nums):
        res = []
        res = deque(res)
        for i in nums:
            if i % 2 == 0:
               res.append(i)
            else:
                res.appendleft(i)
        return list(res)
#Testing part
solution = Solution()
output=solution.exchange(nums)
print(output)
    
#Method 5: method with other logic - 雙指針
#no need to initiate any empty list

class Solution(object):
    def exchange(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

#Testing part
solution = Solution()
output=solution.exchange(nums)
print(output)