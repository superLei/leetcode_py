class Solution:
    # 递归方法，运行直接超时，擦了，看来递归的效率真不是一般的差。
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n - 1) + self.fib((n - 2))

    # 借助额外内存 list 来存储结果队列值，最后直接取出。
    def fib2(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n + 1):
            dp_i = dp[i - 1] + dp[i - 2]
            dp.append(dp_i % 1000000007)
        return dp[n]

    # 动态规划，这个得自己画函数图，一看就清楚了。
    def fib3(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            tmp = a + b
            a = b
            b = tmp
        return a % 1000000007


if __name__ == '__main__':
    obj = Solution()
    # print(obj.fib2(8))
    print(obj.fib3(8))
