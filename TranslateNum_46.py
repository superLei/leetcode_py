class Solution:
    # todo 以后有时间了，再看看错在了哪里。
    # def translateNum(self, num: int) -> int:
    #     num_str = str(num)
    #     length = len(num_str) + 1
    #     dp = [0 for _ in range(length)]
    #     dp[0] = 0
    #     dp[1] = 1
    #     for i in range(2, length):
    #         tmp = num_str[i - 2:i]
    #         if "10" <= tmp <= "25":
    #             dp[i] = dp[i - 1] + dp[i - 2]
    #         else:
    #             dp[i] = dp[i - 1]
    #     print(dp)
    #     return dp[length - 1]

    def translateNum2(self, num: int) -> int:
        num_str = str(num)
        a, b = 1, 1
        length = len(num_str)
        for i in range(2, length + 1):
            tmp = num_str[i - 2:i]
            if "10" <= tmp <= "25":
                tmp_sum = a + b
            else:
                tmp_sum = a
            b = a
            a = tmp_sum
        return a


if __name__ == '__main__':
    a = 122581122
    obj = Solution()
    # print(obj.translateNum(a))
    print(obj.translateNum2(a))
