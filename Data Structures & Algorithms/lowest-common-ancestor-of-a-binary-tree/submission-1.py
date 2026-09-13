# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def get_count(node):
            nonlocal lca
            if not node:
                return 0
            curr_count = get_count(node.left) + get_count(node.right)
            if node is p or node is q:
                curr_count += 1
            if curr_count == 2 and lca is None:
                lca = node
            return curr_count
        get_count(root)
        return lca
        