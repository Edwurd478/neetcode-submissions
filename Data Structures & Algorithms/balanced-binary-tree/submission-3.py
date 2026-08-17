# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root):
        if not root:
            return 0

        h1 = h2 = 0
        h1 = 1 + self.getHeight(root.left)
        h2 = 1 + self.getHeight(root.right)

        #print(root.val, h1, h2)
        return max(h1, h2)

    def checkBal(self, root):
        if not root:
            return True
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        return abs(leftHeight - rightHeight) <= 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.checkBal(root):
            return False
        
        return self.checkBal(root.left) and self.checkBal(root.right)