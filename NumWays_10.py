class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            tmp = a + b
            a = b
            b = tmp
        return a % 1000000007


if __name__ == '__main__':
    obj = Solution()
    print(obj.numWays(0))
    print(obj.numWays(7))
    print(obj.numWays(2))
