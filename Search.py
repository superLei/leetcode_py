from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for x in nums:
            if x == target:
                count += 1
        return count

    # 二分查找，先查找左边界，再查找右边界，计算左右边界长度
    def search2(self, nums: List[int], target: int) -> int:
        mid = len(nums) / 2
        while (mid):
            if target >= mid:
                pass

    # 使用额外内存来保存每个数和对应数出现的次数
    def search3(self, nums: List[int], target: int) -> int:
        map = {}
        for x in nums:
            if map.get(x, 0) > 0:
                map[x] += 1
            else:
                map.setdefault(x, 1)
        return map.get(target, 0)


if __name__ == '__main__':
    obj = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    # print(obj.search(nums, 10))
    print(obj.search3(nums, 9))
