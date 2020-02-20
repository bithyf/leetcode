#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        lenx = len(obstacleGrid)
        leny = len(obstacleGrid[0])
        path = [[] for i in range(lenx)]
        for i in range(lenx):
            path[i] = [0 for i in range(leny)]

        for i in range(len(obstacleGrid) - 1, -1, -1):
            for j in range(len(obstacleGrid[0]) - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    path[i][j] = 0
                elif i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                    path[i][j] = 1
                else:
                    if i == len(obstacleGrid) - 1:
                        path[i][j] = path[i][j + 1]
                    elif j == len(obstacleGrid[0]) - 1:
                        path[i][j] = path[i + 1][j]
                    else:
                        path[i][j] = path[i][j + 1] + path[i + 1][j]

        return path[0][0]
# @lc code=end

