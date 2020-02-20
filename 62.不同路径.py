#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num1 = 1
        num2 = 1
        for i in range(m - 1):
            num1 *= (m + n - 2 - i)
            num2 *= i + 1
        return num1 // num2
# @lc code=end

