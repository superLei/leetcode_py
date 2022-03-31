# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 找出链表中的目标节点和上一个节点，更改上个节点的引用地址即可
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        cur = head.next
        pre = head
        while cur and cur.val != val:
            tmp = cur
            pre = tmp
            cur = cur.next
        if cur:
            pre.next = cur.next
        return head


if __name__ == '__main__':
    a = 1
    b = 2
    # a, b = b, a
    tmp = a
    a = b
    b = tmp
    print(a)
    print(b)
