# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:32:05 2021

@author: Brian
"""


#剑指 Offer 64. 求1+2+…+n
#JZoffer 64. return the sum of consecutive numbers
#Example
#Input: n = 3
#Output: 6

#Input: n = 9
#Output: 45

#要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C)
n = 9

class Solution(object):
    def sumNums(self, n):

    #不能使用乘除法
        return int(n*(n+1)/2)
    
    #recursive method##Important
    #if n == 1: return 1
    #n += self.sumNums(n - 1)
    #return n
    
#testing 
output = Solution().sumNums(n)
print(output)

#Recursive method (more common)

class Solution(object):
    def sumNums(self, n):
    
        if n == 1: return 1
        n += self.sumNums(n - 1)
        return n
    
#testing 
output = Solution().sumNums(n)
print(output)

#Final asnwer (but recursive method is more common)
class Solution(object):
    def __init__(self):
        self.res = 0
    def sumNums(self, n):
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
    
#testing 
output = Solution().sumNums(n)
print(output)