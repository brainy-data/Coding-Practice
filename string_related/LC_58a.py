# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:01:05 2020

@author: Brian
"""

#剑指 剑指 Offer 58 - I. 翻转单词顺序
#JZoffer 58_a_Sentence Reversal
#Example
#Input: "the sky is blue" 
#Output: "blue is sky the"

#Remove unncessary white space as well
#Input: "  hello world!  " 
#Output: "world! hello"

#Input: "a good   example"
#Outpunt: "example good a"

s = "  hello world!  "

#Method 1
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = s.split(' ')
        #this for loop is easier to interpret**
        li = [x for x in li if not x=='']
        return ' '.join(li[::-1])
    
#Testing part
solution=Solution()
output=solution.reverseWords(s)
print(output)

#Method 1.1 - if using split without any argument, it would not return any white space
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = s.split()
        return ' '.join(li[::-1])

#Testing part
solution=Solution()
output=solution.reverseWords(s)
print(output)


#Method 1.2: intruducing one more built-in function /strip/ 
# /strip/ - delete the white spaces in both beginning and the end
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() 
        strs = s.split() 
        strs.reverse() 
        return ' '.join(strs)
    
#Testing part
solution=Solution()
output=solution.reverseWords(s)
print(output)

#Method 2 双指针 - set up i and j to store the result in a list
# A more complicated and mechanical way, does not require many built-in functions
# to study later
class Solution(object):
    def reverseWords(self, s):
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res) # 拼接并返回
    
#Testing part
solution=Solution()
output=solution.reverseWords(s)
print(output)