# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = -1
        if not root:
            return 0

        def getHeight(node):
            if not node:
                return 0
            
            h1 = h2 = 0
            h1 = 1 + getHeight(node.left)
            h2 = 1 + getHeight(node.right)

            return max(h1, h2)
        
        def diameter(node):
            if not node or not node.left and not node.right:
                return 0
            elif not node.left:
                return getHeight(node.right)
            elif not node.right:
                return getHeight(node.left)
            else:
                return getHeight(node.left) + getHeight(node.right)

        return max(diameter(root), max(diameter(root.left), diameter(root.right)))