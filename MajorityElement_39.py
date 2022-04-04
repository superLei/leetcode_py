from typing import List


class Solution:
    """
    时间复杂度：O(N)
    空间复杂度：O(N)
    """

    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for i in range(len(nums)):
            if map.get(nums[i], 0) > 0:
                map[nums[i]] += 1
            else:
                map.setdefault(nums[i], 1)
        for k, v in map.items():
            if v >= len(nums) / 2:
                return k

    # 投票算法，设置众数， 一半为相同数，一半为不同数，不同则抵消票数。相同则相加票数, 投票数为0后则递归上面流程。
    """
    时间复杂度：O(N)
    空间复杂度：O(1)
    """

    def majorityElement2(self, nums: List[int]) -> int:
        votes = 0
        x = nums[0]
        for n in nums:
            if votes == 0:
                x = n
            if n == x:
                votes += 1
            else:
                votes -= 1
        return x


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(obj.majorityElement(nums))
    print(obj.majorityElement2(nums))
