from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        str_list = [str(x) for x in nums]
        result_list = []
        i, j = 0, 0
        while i < len(nums):
            tmp_list = []




if __name__ == '__main__':
    a = [1, 2, 3, 4]
    obj = Solution()
    print(obj.minNumber(a))
