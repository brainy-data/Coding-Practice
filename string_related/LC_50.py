# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 15:46:15 2020

@author: Brian
"""

#JZoffer 50 return the first unique character in a word
#Example
#Input: s = "abaccdeff"
#Output: b

s = "abaccdeff"

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_li = list(s)
        if len(s_li) ==0:
            return " "
        else:
            for _ in range(len(s_li)):
                element = s_li.pop(0)
                if element in s_li:
                    s_li.append(element)
                else:
                    pass
                    return element
            return " "

#testing  
solution=Solution()
output=solution.firstUniqChar(s)
print(output)


#Method 2 - Use a dictionary to record the number of occurences
#This is a more preferred way
class Solution(object):
    def firstUniqChar(self, s):
        dic = {}
        for element in s:
            if element in dic:
                dic[element] = False
            else:
                dic[element] = True
        for element in s:
            if dic[element]: 
                return element
        return ' '
#testing  
solution=Solution()
output=solution.firstUniqChar(s)
print(output)

#Method 2.1- a simplified version
class Solution(object):
    def firstUniqChar(self, s):
        dic = {}
        for element in s:
            dic[element] = not element in dic
        for element in s:
            if dic[element]: return element
        return ' '

#testing  
solution=Solution()
output=solution.firstUniqChar(s)
print(output)