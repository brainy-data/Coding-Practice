# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 23:13:35 2021

@author: Brian
"""

#剑指 Offer  Offer 61. 扑克牌中的顺子
#JZoffer 61. whether a list of number is sequential, 
#while '0' could be any number
#Example
#nums = [0,0,1,2,5]
#Output: True
#
#nums = [1,2,3,4,5]
#Output:True

nums = [0,0,1,2,5]

#Method 1 - Cater for every possibility
class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if 0 in nums:
            nums.sort()
            if len(set(nums)) ==6 - nums.count(0) and nums[-1] - nums[nums.count(0)] <=4: 
                return True
            else:
                return False
        else:
            nums.sort()
            if len(set(nums)) ==5 and nums[-1] - nums[0] ==4:
                return True
            else:
                return False
#Testing part
output= Solution().isStraight(nums)
print(output)

#Method 2

class Solution:
    def isStraight(self, nums):
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue # 跳过大小王
            ma = max(ma, num) # 最大牌
            mi = min(mi, num) # 最小牌
            if num in repeat: return False # 若有重复，提前返回 false
            repeat.add(num) # 添加牌至 Set
        return ma - mi < 5 # 最大牌 - 最小牌 < 5 则可构成顺子 

#Testing part
output= Solution().isStraight(nums)
print(output)

#Method 3
class Solution:
    def isStraight(self, nums):
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子

#Testing part
output= Solution().isStraight(nums)
print(output)