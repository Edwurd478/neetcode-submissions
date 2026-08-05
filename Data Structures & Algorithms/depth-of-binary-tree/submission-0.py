# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        ans = 0
        
        if root:
            queue.append(root)
        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.popleft()
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            ans += 1

        return ans
        
"""
BFS:
- keep track of current depth and node
- add all leaves to queue
"""