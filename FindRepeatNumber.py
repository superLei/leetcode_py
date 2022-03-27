from typing import List


# 查找重复数，关键词"重复"，使用set函数

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        ss = set()
        for i in range(len(nums)):
            ss.add(nums[i])
            if len(ss) < i + 1:
                return nums[i]
        return -1


# python 中使用set进行重复判断时，需要配合len(set)即长度来判断重复数

if __name__ == '__main__':
    a = [2, 3, 1, 0, 2, 5, 3]
    obj = Solution()
    print(obj.findRepeatNumber(a))
