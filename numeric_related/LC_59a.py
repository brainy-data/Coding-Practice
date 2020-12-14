# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:45:16 2020

@author: Brian
"""

nums = [1,3,-1,-3,5,3,6,7]
k = 3

#Method 1.1
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        max_lst = []
        for idx in range(len(nums)-k+1):
            slice = nums[idx:idx+k]
            tmp_max = max(slice)
            max_lst.append(tmp_max)
        return max_lst
#Testing part
solution= Solution()
output=solution.maxSlidingWindow(nums, k)
print(output)

#Method 1.2
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if nums==[] or k==0:
            return []
        else:
            res = []
            for i in range(len(nums) - k + 1):
                partial = nums[i : i+k]
                res.append(max(partial))
            return res
#Testing part
solution= Solution()
output=solution.maxSlidingWindow(nums, k)
print(output)

#Comment
#Method 1 is a rather brute force method

#Method 2 单调队列 - more efficient logic, but rather complicated
#To study later

