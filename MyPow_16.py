class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            for i in range(n):
                x *= x
        elif n < 0:
            pass
        else:
            return 1


if __name__ == '__main__':
    obj = Solution()
