# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 00:06:55 2021

@author: Brian
"""

#剑指 Offer 57 - 和为s的两个数字
#JZoffer 57 - find the sum values matched to target
#Example
#nums = [2,7,11,15], target = 9
#Output: [2,7] or [7,2]

nums = [10,26,30,31,47,60]
target = 40

#Method - 雙指針方法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        b = len(nums) - 1
        while a < b:
            s = nums[a] + nums[b]
            if s > target: 
                b-=1
            elif s < target:
                a+=1
            else: return [nums[a],nums[b]]
        return []
    
#testing part
output = Solution().twoSum(nums, target)
print(output)
