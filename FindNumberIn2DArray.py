class Solution(object):
    # 只会暴力查找
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

    # 把二维数组倒过来看，从下往上进行判断，大于target则向上一行，小于target则向右一列，相等则返回True
    # 充分利用了有序这个特点
    def findNumberIn2DArray2(self, matrix, target):
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False


if __name__ == '__main__':
    list_t = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(list_t)
    obj = Solution()
    print(obj.findNumberIn2DArray(list_t, 3))
