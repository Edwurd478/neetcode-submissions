# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root):
        if not root:
            return

        self.traverse(root.left)

        if self.counter == self.k:
            self.ans = root.val
            self.counter += 1
            return
        elif self.counter > self.k:
            return

        self.counter += 1
        self.traverse(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.k = k-1
        self.ans = -1
        self.traverse(root)

        return self.ans