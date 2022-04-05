import sys
from typing import List


class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_num = 0
        a, b = 0, 0
        n = len(nums)
        while a < n:
            b = a + 1
            while b < n:
                if a >= b:
                    b += 1
                else:
                    max_num = max(max_num, nums[b] - nums[a])
                b += 1
            a += 1
        return max_num

    def maxProfit2(self, nums: List[int]) -> int:
        min_num = sys.maxsize
        lirui = 0
        n = len(nums)
        for i in range(n):
            min_num = min(min_num, nums[i])
            lirui = max(lirui, nums[i] - min_num)
        return lirui


if __name__ == '__main__':
    obj = Solution()
    nums = [7, 1, 5, 3, 6, 4]
    # nums = [7, 6, 4, 3, 1]
    print(obj.maxProfit2(nums))
