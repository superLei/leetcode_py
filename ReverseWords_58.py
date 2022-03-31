class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.strip().split()
        s_list = [x for x in s_list]
        return ' '.join(s_list[::-1])


if __name__ == '__main__':
    obj = Solution()
    s = "I am a            student.  "
    print(obj.reverseWords(s) + "****")
    print(s.strip() + "****")
