from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = len(nums) - 1
        while j >= 0 and nums[j] > target:
            j -= 1
        i = 0
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                return [nums[i], nums[j]]


if __name__ == '__main__':
    obj = Solution()
    nums = [2, 7, 11, 15]
    print(obj.twoSum(nums, 3))
