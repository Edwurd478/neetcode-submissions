# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def get_height(node):
            nonlocal result
            if not node:
                return 0
            leftheight = get_height(node.left)
            rightheight = get_height(node.right)
            result = max(result, leftheight + rightheight)

            return max(leftheight, rightheight) + 1
        
        get_height(root)
        return result