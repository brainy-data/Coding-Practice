# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:30:59 2020

@author: Brian
"""

#剑指 Offer 42- 连续子数组的最大和
#JZoffer 42. return max sum from all sub-array
#Example
#Input: [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Further explanation: sum of [4,-1,2,1] is 6, which is the max in the list.


#Method: concept of dynamic programming could be applied here
#continue to add on as long as the rolling sum is positive, 
#then return the max from the calculation results


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[i] += max(nums[i - 1],0)
        return max(nums)
    
def offer_42(nums):
    solution = Solution()
    output = solution.maxSubArray(nums)

    print(output)
    
offer_42(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])