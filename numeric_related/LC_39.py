


#剑指 Offer 39-  数组中出现次数超过一半的数字
#JZoffer 39. return the majority number
#Example
#nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
#Output: 2 

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in set(nums):
            if nums.count(num) > len(nums)*0.5:
                return num
    
nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    
solution = Solution()
output = solution.majorityElement(nums)
print(output)

#other methods
#method 1 : 摩尔投票法 (Moore majority vote)

class Solution:
    def majorityElement(self, nums):
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x

solution = Solution()
output = solution.majorityElement(nums)
print(output)

#method 2: given a list with only one major number,  
#the answer must lie in the exact middle of the sorted number list 
    
class Solution:
    def majorityElement(self, nums):
        return sorted(nums)[int(len(nums)/2)]


solution = Solution()
output = solution.majorityElement(nums)
print(output)