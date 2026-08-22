# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def findPath(node, currSum):
            currSum += node.val
            if not node.left and not node.right:
                return True if currSum == targetSum else False
            
            leftPath = rightPath = False
            if node.left:
                leftPath = findPath(node.left, currSum)
            if node.right:
                rightPath = findPath(node.right, currSum)
            
            return leftPath or rightPath
        
        return findPath(root, 0)