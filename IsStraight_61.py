class Solution:
    def isStraight(self, nums):
        nums.sort()
        zero_count = 0
        not_one_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                continue
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                return False
            if i < len(nums) - 1 and nums[i + 1] - nums[i] > 3:
                return False
            if i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                continue
            if i < len(nums) - 1:
                not_one_count += 1
        if not_one_count <= zero_count:
            return True
        return False


if __name__ == "__main__":
    obj = Solution()
    # nums = [1, 2, 3, 0, 5, 7]
    # nums = [0, 0, 2, 2, 5]
    nums = [10, 11, 0, 12, 6]
    print(obj.isStraight(nums))
