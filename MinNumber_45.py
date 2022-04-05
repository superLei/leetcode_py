from typing import List


class Solution:

    # 此方法会超时
    def minNumber(self, nums: List[int]) -> str:
        """
        1. 转字符数组。2.  列出所有的组合并放到数组中。3. 排序数组，返回最小值。
        :param nums:
        :return:
        """
        res = set()
        str_nums = [str(x) for x in nums]

        def dg(x):
            if x == len(str_nums) - 1:
                res.add(''.join(str_nums))
                return
            for i in range(len(str_nums)):
                str_nums[i], str_nums[x] = str_nums[x], str_nums[i]
                dg(x + 1)
                str_nums[i], str_nums[x] = str_nums[x], str_nums[i]

        dg(0)
        res = list(res)
        res.sort()
        return res[0]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # a = [1, 2, 3, 4]
    obj = Solution()
    print(obj.minNumber(a))
