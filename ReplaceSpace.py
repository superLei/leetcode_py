class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

    def replaceSpace2(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ':
                res.append('%20')
            else:
                res.append(c)
        return "".join(res)


if __name__ == "__main__":
    s = "We are happy."
    obj = Solution()
    print(obj.replaceSpace(s))
    print(obj.replaceSpace2(s))
