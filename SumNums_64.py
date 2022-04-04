class Solution:
    def sumNums(self, n):
        if n == 1:
            return 1
        return self.sumNums(n - 1) + n

    def sumNums2(self, n):
        return n and self.sumNums(n - 1) + n


if __name__ == '__main__':
    obj = Solution()
    print(obj.sumNums2(3))
