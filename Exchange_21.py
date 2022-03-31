from typing import List


# 特性，整数只分奇数和偶数
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l1 = []
        l2 = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        return l1 + l2

    # 首尾指针
    def exchange2(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0 and nums[j] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] % 2 != 0:
                i += 1
            if nums[j] % 2 == 0:
                j -= 1
        return nums


if __name__ == "__main__":
    print(1)
    nums = [1, 2, 3, 4, 5]
    obj = Solution()
    print(obj.exchange(nums))
    print(obj.exchange2(nums))
