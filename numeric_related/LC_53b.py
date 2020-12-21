# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:57:01 2020

@author: Brian
"""

#剑指 Offer 53b- 0～n-1中缺失的数字
#JZoffer 42. return the missing number of a list
#Example
#Input: [0,1,2,3,4,5,6,7,9]
#Output: 8


#Method 1: straightforward method
nums = [0,1,2,3,4,5,6,7,9]

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
#testing
solution=Solution()
output = solution.missingNumber(nums)
print(output)


#Method 2- calculate the difference between expected sum and current sum
class Solution(object):
    def missingNumber(self, nums):

        return sum(range(len(nums)+1)) - sum(nums)
#testing
solution=Solution()
output = solution.missingNumber(nums)
print(output)

#Method 3-二分法
#cross check index number and corresponding value, 
# Checking starts from middle point everytime

class Solution(object):
    def missingNumber(self, nums):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i
    
#testing
solution=Solution()
output = solution.missingNumber(nums)
print(output)