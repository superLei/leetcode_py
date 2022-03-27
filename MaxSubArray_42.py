import sys
from typing import List


class Solution:
    # 动态规则好难，状态转移方程找出来，解题思路就明确了，还有就是比较，使用变量保存上次的结果（这个变量可以共用）
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        before = nums[0]

        for i in range(1, len(nums)):
            if before > 0:
                before += nums[i]
            else:
                before = nums[i]
            max_num = max(before, max_num)
        return max_num


if __name__ == '__main__':
    obj = Solution()
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-2, 1]
    nums = [0, -1]
    # nums = [1]
    print(obj.maxSubArray(nums))
