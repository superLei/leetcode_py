class Solution(object):
    # 循环一次，记录所有字符及它出现的次数，再返回只出现一次的字符
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = {}
        for c in s:
            if map.get(c, -1) > 0:
                map[c] += 1
            else:
                map.setdefault(c, 1)
        for k, v in map.items():
            if v == 1:
                return k
        return ' '

    # 打算使用双指针，有问题，费
    def firstUniqChar2(self, s):
        i, j = 1, 0
        while j < len(s) - 1 and i < len(s) - 1:
            if s[j] != s[i]:
                i += 1
            else:
                j += 1
                i = j + 1
        return s[j]


if __name__ == '__main__':
    obj = Solution()
    s = "abaccdeff"
    # s = "leetcode"
    # print(obj.firstUniqChar(s))
    print(obj.firstUniqChar2(s))
