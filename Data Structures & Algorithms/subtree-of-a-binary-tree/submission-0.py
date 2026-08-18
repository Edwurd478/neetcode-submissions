# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isEqual(tree1, tree2):
            if not tree1 and not tree2:
                return True
            elif not tree1 or not tree2:
                return False
            
            return (tree1.val == tree2.val) and isEqual(tree1.left, tree2.left) and isEqual(tree1.right, tree2.right)
        
        nodes = deque()
        nodes.append(root)
        while len(nodes) > 0:
            for i in range(len(nodes)):
                currNode = nodes.popleft()
                if isEqual(currNode, subRoot):
                    return True
                if currNode.left:
                    nodes.append(currNode.left)
                if currNode.right:
                    nodes.append(currNode.right)
        
        return False

