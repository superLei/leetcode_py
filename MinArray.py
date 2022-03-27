class Solution(object):
    # 数组旋转后，肯定会有后一个数减前一个数大于0的情况，所以目的是找到降落点，如果没有降落点就返回第一个数
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        target = numbers[0]
        count = 0
        for i in range(1, len(numbers)):
            if target - numbers[i] <= 0:
                target = numbers[i]
                count += 1
            else:
                return numbers[i]
        if count == len(numbers) - 1:
            return numbers[0]


if __name__ == '__main__':
    # numbers = [3, 4, 5, 1, 2]
    # numbers = [2, 2, 2, 0, 1]
    # numbers = [2, 2, 2, 2, 1]
    numbers = [2, 2, 2, 2, 2]
    obj = Solution()
    print(obj.minArray(numbers))
