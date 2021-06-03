#剑指 Offer 62-  圆圈中最后剩下的数字
#JZoffer 39. return the last remaining number
# a list of number starting from 0 to n, delete the "m"th number each time
# (count starting from the next number after deletion)
#Example
#n = n = 5, m = 3
#Output: 3 (after the deletion of 2、0、4、1)


#Method - Dynamic Programming

class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x

n = 5
m = 3

solution = Solution()
output = solution.lastRemaining(n,m)
print(output)