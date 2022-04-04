from typing import List


class Solution:
    """
    时间复杂度: O(Nlog(N))
    空间复杂度: O(1)
    """

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[0:k]

    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        print(arr)

        def quick_sort(arr, l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            quick_sort(arr, l, i - 1)
            quick_sort(arr, i + 1, r)
            print(arr)

        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    # def quick_sort(self, nums, left, right):
    #     if left >= right:
    #         return
    #     i = left
    #     j = right
    #     while i < j:
    #         while i < j and nums[i] >= nums[left]:
    #             i += 1
    #         while i < j and nums[j] <= nums[left]:
    #             j -= 1
    #         nums[i], nums[j] = nums[j], nums[i]
    #     # nums[i], nums[left] = nums[left], nums[i]
    #     nums[left], nums[i] = nums[i], nums[left]
    #     self.quick_sort(nums, left, i - 1)
    #     self.quick_sort(nums, i + 1, right)


if __name__ == '__main__':
    obj = Solution()
    arr = [0, 1, 2, 1]
    k = 1
    print(obj.getLeastNumbers(arr, k))
    print(obj.getLeastNumbers2(arr=arr, k=k))
