# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre  # 下一个节点的指向改为上个节点
            pre = cur  # 暂存当前节点
            cur = tmp  # 当前的节点访问下一个节点
        return pre
