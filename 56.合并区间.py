#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda num: num[0])
        if len(intervals) == 0 or len(intervals[0]) == 0:
            return
        f = intervals[0][0]
        b = intervals[0][1]

        nums = 1
        while nums < len(intervals):
            if b >= intervals[nums][0] >= f:
                b = max(b, intervals[nums][1])
                intervals[nums - 1][1] = b
                del intervals[nums]
            else:
                f = intervals[nums][0]
                b = intervals[nums][1]
                nums += 1
        return intervals
# @lc code=end

