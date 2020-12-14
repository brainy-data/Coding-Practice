# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:29:57 2020

@author: Brian
"""

#剑指 Offer 11. 旋转数组的最小数字
#JZoffer 11. return the minimum value in a semi-sorted list
#Example 1
#Input:  [3,4,5,1,2]
#Output: 1

#Example 2
#Input:  [2,2,2,0,1]
#Output: 0

numbers = [2,2,3,0,1]

#Method 1
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        return min(numbers)

#Testing part
solution = Solution()
output=solution.minArray(numbers)
print(output)

#If min function is not allowed...
#Method 2 - 二分法, this method is more effective when dealing with long list of numebrs
class Solution(object):
    def minArray(self, numbers):

        left, right = 0, len(numbers) - 1

        while left < right:
            pivot = (right + left) // 2
            if numbers[pivot] > numbers[right]:
                left = pivot + 1
            elif numbers[pivot] < numbers[left]:
                right = pivot
            else:
                right -= 1

        return numbers[left]

#Testing part
solution = Solution()
output=solution.minArray(numbers)
print(output)
