#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        num = []
        lenx = len(matrix)
        if lenx == 0:
            return num
        leny = len(matrix[0])
        sublenx = 0
        subleny = 0
        length = min(lenx, leny)
        for k in range(length // 2):
            sublenx = lenx - 2 * k - 1
            subleny = leny - 2 * k - 1
            for i in range(subleny):
                num.append(matrix[k][k + i])
            for i in range(sublenx):
                num.append(matrix[k + i][k + subleny])
            for i in range(subleny):
                num.append(matrix[k + sublenx][k + subleny - i])
            for i in range(sublenx):
                num.append(matrix[k + sublenx - i][k])
        if length % 2 != 0:
            if lenx < leny:
                i = lenx // 2
                for j in range(i, leny - i):
                    num.append(matrix[i][j])
            else:
                j = leny // 2
                for i in range(j, lenx - j):
                    num.append(matrix[i][j])
        return num
# @lc code=end

