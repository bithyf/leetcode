#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
# 我又成功了

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max = 1
        for i in range(len(nums)):
            max -= 1
            if nums[i] > max:
                max = nums[i]
            if max == 0 and i < len(nums) - 1:
                return False
        return True

# @lc code=end

