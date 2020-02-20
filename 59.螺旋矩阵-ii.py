#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 1:
            return []
        '''生成矩阵'''
        matrix = [[] for i in range(n)]
        for i in range(n):
            matrix[i] = [0 for i in range(n)]
        num = 1
        for k in range(n // 2):
            length = n - 2 * k - 1
            for i in range(length):
                matrix[k][k + i] = num
                num += 1
            for i in range(length):
                matrix[k + i][k + length] = num
                num += 1
            for i in range(length):
                matrix[k + length][k + length - i] = num
                num += 1
            for i in range(length ):
                matrix[k + length - i][k] = num
                num += 1
        if n % 2 != 0:
            matrix[n // 2][n // 2] = num
        return matrix

# @lc code=end

