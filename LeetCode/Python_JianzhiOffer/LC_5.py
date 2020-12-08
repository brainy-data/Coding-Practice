# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:32:54 2020

@author: Brian
"""

#剑指 Offer 05. 替换空格
#JZoffer 05. Replacing whitespaces with other characters
#Example
#Input: s = "We are happy."
#Output: "We%20are%20happy."

#Method 1: Use built-in replace function
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        #replace(old,new,count)
        return s.replace(' ','%20')
    
s="We are happy"

solution=Solution()
output=solution.replaceSpace(s)

print(output)

#Method 2: Split the string with whitespaces and then join them back with %20
class Solution(object):
    def replaceSpace(self, s):
        #after split, the datatype becomes a list, and use join() with list
        return '%20'.join(s.split(' '))
    
s="We are happy"

solution=Solution()
output=solution.replaceSpace(s)

print(output)

#Method 3: initiate an empty string and use if else to get the result

class Solution(object):
    def replaceSpace(self, s):
        res=[]
        for i in s:
            if i == " ":res.append("%20")
            else: res.append(i)
            #the result is a 'list' of strings, so still need to join all elements in the list together
        return ''.join(res)    

s="We are happy"

solution=Solution()
output=solution.replaceSpace(s)

print(output)

##*Method 3.1: more reader-friendly and simplified way of method 3*

class Solution(object):
    def replaceSpace(self, s):
        return ''.join('%20' if i==' ' else i for i in s)    

s="We are happy"

solution=Solution()
output=solution.replaceSpace(s)

print(output)


#Method 4: initiate an empty string and use if else

class Solution(object):
    def replaceSpace(self, s):
        res=""
        for i in s:
            if i == " ":res += "%20"
            else: res += i
            #unlike method 3, no need to use join here
        return res

s="We are happy"

solution=Solution()
output=solution.replaceSpace(s)

print(output)
