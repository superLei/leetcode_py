from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        while root.left or root.right:
            res2 = []
            if root.left:
                res2.append(root.left)
                root = root.left
                self.levelOrder(root)
            if root.right:
                res2.append(root.right)
                root = root.right
                self.levelOrder(root)
            res.append(res2)
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.levelOrder())
