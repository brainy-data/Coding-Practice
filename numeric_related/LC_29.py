# 剑指 Offer 29-  顺时针打印矩阵
# JZoffer 29. spiral-matrix
# Print out the element in a matrix with a spiral direction
# Example
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output = [1,2,3,6,9,8,7,4,5]
# Reference: https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg



# Method: Break it into 4 steps
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i]) # Step 1: left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r]) # Step 2: top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i]) # Step 3: right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l]) # Step 4: bottom to top
            l += 1
            if l > r: break
        return res

# Testing part

matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
output = solution.spiralOrder(matrix)
print(output)