# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:53:45 2020

@author: Brian
"""

#剑指 Offer 03. 数组中重复的数字
#JZoffer 05. Finding duplicated number
#Given a list of integers, 
#return 'any' integer which appears more than once
#Example
#Input:  [2, 3, 1, 0, 2, 5, 3]
#Output: 2 or 3
nums = [2, 3, 1, 0, 2, 5, 3]

#Method 1 - initiate an empty dictionary and then check if the number is duplicated by adding them one by one
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            else:
                return i
        
#Testing part
solution=Solution()
output=solution.findRepeatNumber(nums)
print(output)

#Method 2 - initiate an empty set and then check if the number is duplicated by adding them one by one
class Solution(object):
    def findRepeatNumber(self, nums):
        s = set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)
        
#Testing part
solution=Solution()
output=solution.findRepeatNumber(nums)
print(output)

#Method 2 - Double for loop method, 
#strightforward but almost the most inefficient method 
#exceed time limits in coding test
class Solution(object):
    def findRepeatNumber(self, nums):
        size = len(nums)
        for i in range(size):
           for j in range (i+1, size):
               if nums[i] == nums[j]:return nums[i]
        
#Testing part

solution=Solution()
output=solution.findRepeatNumber(nums)
print(output)

##Variation 1 - find 'all' duplicated integers
#Input:  [2, 3, 1, 0, 2, 5, 3]
#Output: [2,3]

class Solution(object):
    def findRepeatNumber(self, nums):
        s = set()
        d = set()
        for i in nums:
            if i in s:
                d.add(i)
            else:
                s.add(i)
        
        return list(d)

#Testing part
nums = [2, 3, 1, 0, 2, 5, 3]
solution=Solution()
output=solution.findRepeatNumber(nums)
print(output)

##Variation 2 - find non-duplicated integers
#Input:  [2, 3, 1, 0, 2, 5, 3]
#Output: [1,0,5]


class Solution(object):
    def findRepeatNumber(self, nums):
        s = set()
        d = set()
        for i in nums:
            if i in s:
                d.add(i)
            else:
                s.add(i)
        
        return list(s.difference(d)) 

#Testing part
nums = [2, 3, 1, 0, 2, 5, 3]
solution=Solution()
output=solution.findRepeatNumber(nums)
print(output)



##Variation 3 - find 'the most' duplicated integers
#Input:  [2, 3, 1, 0, 2, 5, 3, 3]
#Output: 3

class Solution(object):
    def findRepeatNumber(self, nums):
        s = list()
        d = list()
        for i in nums:
            if i in s:
                d.append(i)
            else:
                s.append(i)
        
        return max(set(d), key= d.count)

#Testing part
nums = [2, 3, 1, 0, 2, 5, 3, 3]
solution=Solution()
output=solution.findRepeatNumber(nums)
print(output)