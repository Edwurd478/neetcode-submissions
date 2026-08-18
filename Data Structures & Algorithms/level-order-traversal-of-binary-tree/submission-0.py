# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nodes = deque()
        nodes.append(root)
        level = 0
        ans = []
        while len(nodes) > 0:
            ans.append([])
            for i in range(len(nodes)):
                currNode = nodes.popleft()
                ans[level].append(currNode.val)
                if currNode.left:
                    nodes.append(currNode.left)
                if currNode.right:
                    nodes.append(currNode.right)
            
            level += 1
        
        return ans