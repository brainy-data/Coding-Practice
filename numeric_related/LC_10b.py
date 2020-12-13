# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:17:31 2020

@author: Brian
"""

#剑指 Offer 10b- 青蛙跳台阶问题
#JZoffer 10b.  calculate the number of leaping combination
#A frog can leap 1 stair step or 2 star steps at a time.
#Given a stair of 'n' steps, return the number of leaping combinations.
#Example
#Input: 2
#Output: 2
#Input: 7
#Output:21
#Input: 0
#Output:1

n=7
#Ratinale: This problem ccould be viewed as a Fibonacci sequence.
#For instance, for a stair with 5 steps, the number of combination would be 
#the sum of junping (stair with 3 steps) and (stair with 4 steps).

#Method 1: Dynammic Programming
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
#Testing part
solution=Solution()
output=solution.numWays(n)
print(output)

 
#Method 2a
class Solution(object):
    def numWays(self, n):
        initial = [1,1]
        if n<=1:
            return 1
        else:
            for _ in range (n-2):
                initial.append(sum(initial))
                del initial[0]
            return sum(initial)%1000000007
#Testing part
solution=Solution()
output=solution.numWays(n)
print(output)

#Method 2b
class Solution(object):
    def numWays(self, n):
        initial = [1,1]
        if n<=1:
            return 1
        else:
            for _ in range (n-1):
                initial.append(initial[-1]+initial[-2])
            return (initial[-1])%1000000007
#Testing part
solution=Solution()
output=solution.numWays(n)
print(output)