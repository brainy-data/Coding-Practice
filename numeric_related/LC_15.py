# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:50:54 2020

@author: Brian
"""

#剑指 Offer 15. 二进制中1的个数
#JZoffer 15. count number of '1's in binary system
#Example
#Input:  11 
#Output: 3
#Note: 11 is [1011] in binary system

n=11
#Method 1 - strighforward one
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #convert into binary number (string) and count number of '1's
        #if want to count '0's, need to minus 1 since binary conversion will have '0b' at the beginning of the string
        return  bin(n).count("1") 

#Testing part
solution=Solution()
output=solution.hammingWeight(n)
print(output)

#Other methods - realted to bitwise operation (位運算)
#To perform count operations without using count function
#To study later**

class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

solution=Solution()
output=solution.hammingWeight(n)
print(output)

class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
    
solution=Solution()
output=solution.hammingWeight(n)
print(output)
