class Solution(object):
    # 使用循环二分查找, 分别查找左右区间 ,
    # 若 nums[m]=m ，则 “右子数组的首位元素” 一定在闭区间 [m + 1, j][m+1,j] 中，因此执行 i = m + 1
    # 若 nums[m]不=m ，则 “左子数组的末位元素” 一定在闭区间 [i, m - 1][i,m−1] 中，因此执行 j = m - 1 (这里为什么减1，估计是最后为了退出循环)
    # [L,R] 区间内计算中间值公式为 m = (L+R) /2
    #
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (j + i) // 2
            if m == nums[m]:
                i = m + 1
            else:
                j = m - 1  # 这里是重点，不太懂
        return i

    # 投机取巧， 因为是连续且递增为1的数列，所以使用数学方法， 应总和  - 实际总和 = 缺失的数
    def missingNumber2(self, nums):

        sum = 0
        length = len(nums)
        for x in nums:
            sum += x

        act_sum = (0 + length) * (length + 1) / 2
        return (act_sum - sum)


if __name__ == '__main__':
    obj = Solution()
    nums = [0, 1, 2, 3, 5, 6, 7, 8, 9]
    print(obj.missingNumber(nums))
    # print(obj.missingNumber2(nums))
