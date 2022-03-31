# Definition for singly-linked list.
from typing import List


class SingleNode:
    """单节点"""

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: SingleNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


if __name__ == "__main__":
    # obj = Solution()
    # obj.reversePrint()
    a = [1, 2, 3]
    print(a[::-1])
