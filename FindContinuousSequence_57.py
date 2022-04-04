from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        n = target // 2 + 1
        l = 1
        r = n + 1
        res = []
        while l < n:
            tmp = []
            sums = 0
            for i in range(l, r):
                sums += i
                tmp.append(i)
                if sums == target:
                    res.append(tmp)
                    break
                if sums > target:
                    tmp = []
                    break
            l += 1

        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.findContinuousSequence(15))
