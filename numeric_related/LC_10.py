# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:45:24 2020

@author: Brian
"""

#剑指 Offer 10- I. 斐波那契数列
#JZoffer 10. return the nth number from Fibonacci sequence
#Example
#Fibonacci sequence:[0,1,1,2,3,...]
#Input: 2
#Output: 1
#Input: 5
#Output:5

#答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#return the answer of reminder when the reuslt is divided by 1000000007
 

n=5
#Method 1: initiate a list to store the current result 
#(adding new number while deleting the first number)
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        li = [0,1]
        if n > 0:
            for i in range(n-2):
                li.append(sum(li))
                del li[0]
            return sum(li)%1000000007
        else:
            return 0

#Testing part
solution=Solution()
output=solution.fib(n)
print(output)

#Method 2: same logic but store all results in the list
      
class Solution(object):
    def fib(self, n):

        li = [0,1]
        if n > 0:
            for i in range(n-2):
                li.append(li[-1]+li[-2])
            return (li[-1]+li[-2])%1000000007
        else:
            return 0

#Testing part
solution=Solution()
output=solution.fib(n)
print(output)
        
#Method from others - Dynammic Programming
#Quite a fancy way, To learn later
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

#Testing part
solution=Solution()
output=solution.fib(n)
print(output)