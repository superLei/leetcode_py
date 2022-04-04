from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        if n == 1:
            return [s]
        res = []
        for i in range(n):
            # 首字符
            l = s[i]
            # 根据首字符生成新的字符串
            new_s = s
            new_s[0], new_s[i] = s[i], s[0]
            # 每次结果字符
            result = ''
            j = n - 1
            new_s_2 = new_s
            while j <= i:
                res.append(new_s_2)
                new_s_2[j], new_s_2[j - 1] = new_s_2[j - 1], new_s_2[j]
                res.append(new_s_2)

    def permutation22(self, s: str) -> List[str]:
        res = []
        c = list(s)

        def dfs(x):
            if x == len(s) - 1:
                res.append(''.join(c))
            tmp_set = set()
            for i in range(x, len(c)):
                if c[i] in tmp_set: return
                tmp_set.add(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x + 1)
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return res


if __name__ == '__main__':
    obj = Solution()
    a = 'abc'
    print(obj.permutation22(a))
