# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:45:47 2020

@author: Brian
"""

#剑指 Offer 58 - II. 左旋转字符串
#JZoffer 58_b_Rearrange String Charaters
#Example
#Input: s = "abcdefg", n = 2  
#Output: "cdefgab"


#Python solution
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[:n]

#Testing Part
s = "acbdefg"
n = 2    

solution = Solution()
output = solution.reverseLeftWords(s, n)

print(output)


###Solution from others###
#What if string slicing (e.g. s[n:])  is prohibited...
#Can initiate an emply list and use append 

class Solution(object):
    def reverseLeftWords(self, s, n):
        res = []
        for i in range(n,len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)

#Testing part
s='acbdefg'
n=2
solution = Solution()
output = solution.reverseLeftWords(s, n)

print(output)


#What if join is prohibited...
#Can initiate an emply"string" and use +=

class Solution(object):
    def reverseLeftWords(self, s, n):
        res = ""
        for i in range(n,len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res

#Testing part
s='acbdefg'
n=2
solution = Solution()
output = solution.reverseLeftWords(s, n)
print(output)


###Variation_1###
#rotate starting from right hand side rather than left hand side
#Example
#Input: s = "abcdefg", n = 2  
#Output: "fgabcde"

#Python solution
class Solution(object):
    def reverseLeftWords(self, s, n):
        m = len(s) - n
        return s[m:] + s[:m]

#Testing Part
s = "acbdefg"
n = 2    

solution = Solution()
output = solution.reverseLeftWords(s, n)

print(output)


#However, this method requires an additional variable "m"
#To avoid an additional variable, we may use the negative sign in Python string slicing 

#Python solution
class Solution(object):
    def reverseLeftWords(self, s, n):
        return s[-n:] + s[:-n]

#Testing Part
s = "acbdefg"
n = 2    

solution = Solution()
output = solution.reverseLeftWords(s, n)

print(output)


###Variation_2###
#String reversal (mirror reverse)
#Example
#Input: s = "abcdefg"  
#Output: "gfedcba"

##One trick here is to take advantage of the syntax: seq[start:end:step]
class Solution(object):
    def reverseLeftWords(self, s):
        return s[::-1]

#Testing Part
s = "acbdefg"   

solution = Solution()
output = solution.reverseLeftWords(s)

print(output)


#If slicing is prohibited, another way is to apply the built-in reversed function and join them
class Solution(object):
    def reverseLeftWords(self, s):
        return ''.join(reversed(s))

#Testing Part
s = "acbdefg"   

solution = Solution()
output = solution.reverseLeftWords(s)

print(output)