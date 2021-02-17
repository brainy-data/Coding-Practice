# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:22:51 2021

@author: Brian
"""

#剑指 Offer 57-  和为s的连续正数序列
#JZoffer 57. list of consecutive numbers return the sum as target
#Example
#Input: target = 9
#Output: [[2,3,4],[4,5]]

#Input: target = 15
#Output: [[1,2,3,4,5],[4,5,6],[7,8]]

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        index1 = 1
        index2 = 2
        all_ans = []

        while index2 <= target //2 + 1:
            cur_sum = sum(list(range(index1,index2+1)))
            if cur_sum < target:
                index2 +=1
            elif cur_sum > target:
                index1 +=1
            else:
                all_ans.append(list(range(index1,index2+1)))
                index2 +=1
        return all_ans
    

#testing part
target = 15
output = Solution().findContinuousSequence(target)
print(output)
