class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s1 = s[:n]
        s2 = s[n:]
        return s2 + s1

    def reverseLeftWords2(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(0, n):
            res.append(s[i])
        return "".join(res)


if __name__ == "__main__":
    s = 'abcdefg'
    obj = Solution()
    res = obj.reverseLeftWords(s, 2)
    res2 = obj.reverseLeftWords(s, 2)
    print(res)
    print(res2)
