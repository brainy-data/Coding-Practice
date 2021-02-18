# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:38:50 2021

@author: Brian
"""

#剑指 Offer 04. 二维数组中的查找
#JZoffer 04 in a 2d matrix, check if the target number exists
#each row and each column is in ascending order
#Example
#matrix  = [
#  [1,   4,  7, 11, 15],
#  [2,   5,  8, 12, 19],
#  [3,   6,  9, 16, 22],
#  [10, 13, 14, 17, 24],
#  [18, 21, 23, 26, 30]
#]
#Input: 5
#Output: True

#Input : 20 
#Output: False

matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]

target = 5
#Method 1
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        list_boo = []
        for row_idx in range(len(matrix)):
            if len(matrix[row_idx]) > 0:
                if matrix[row_idx][0] <= target and  matrix[row_idx][-1] >= target:
                        list_boo.append(target in matrix[row_idx])
        return(True in list_boo)
      
#testing
output = Solution().findNumberIn2DArray(matrix, target)
print(output)
    
#Method 2
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        bool_list = []
        for row_idx in range(len(matrix)):
            if len(matrix[row_idx]) > 0:
                if matrix[row_idx][0] <= target and  matrix[row_idx][-1] >= target:
                        if target in matrix[row_idx]:
                            bool_list.append(True)
                            break
        return (True in bool_list)
#testing
output = Solution().findNumberIn2DArray(matrix, target)
print(output)
    
#Other method : Similar to Two Pointers Method 
#first point to bottom left number, if it is greater than target, goes up one row (i)
#if it is smaller than target, goes to right column (j)
class Solution:
    def findNumberIn2DArray(self, matrix, target):
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            else: return True
        return False
#testing
output = Solution().findNumberIn2DArray(matrix, target)
print(output)