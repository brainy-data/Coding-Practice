# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:57:01 2020

@author: Brian
"""

#剑指 Offer 53a- 在排序数组中查找数字 I
#JZoffer 42. count occurence of an element in a list
#Example
#Input: nums = [5,7,7,8,8,10], target = 8
#Output: 2

#Method 1: straightforward method (use count)
nums = [5,7,7,8,8,10]
target = 8

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return nums.count(target)
    
#testing
solution=Solution()
output=solution.search(nums, target)
print(output)

#Method 2 - can use 二分法 to solve given that the list is sorted

class Solution(object):
    def search(self, nums, target):

        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target: return 0
        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        return right - left - 1

#testing
solution=Solution()
output=solution.search(nums, target)
print(output)