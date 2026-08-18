# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)
        if (val1 < root.val and val2 > root.val) or root == p or root == q:
            return root
        
        if val1 < root.val and val2 < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)