from typing import List


class Solution:
    """
    时间复杂度: O(log(N))
    空间复杂度: O(1)
    """

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[0:k]

    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        pass


if __name__ == '__main__':
    obj = Solution()
    arr = [0, 1, 2, 1]
    k = 1
    print(obj.getLeastNumbers(arr, k))
