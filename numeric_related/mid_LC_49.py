# 剑指 Offer 62 - 丑数
# JZoffer 62. return the "n"th product of 2,3 or 5 in ascending order
#E xample
# n = 10
# Output: 12
# Demo: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]
    
n = 10
    
solution = Solution()
output = solution.nthUglyNumber(n)
print(output)
