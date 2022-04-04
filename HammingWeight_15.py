class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if n & (1 << i):
                count += 1
        return count


if __name__ == '__main__':
    obj = Solution()
    print(obj.hammingWeight(5))
    print(1 & 0)
    print(1 & 1)
    print(0 & 0)
    print(1 >> 1)
