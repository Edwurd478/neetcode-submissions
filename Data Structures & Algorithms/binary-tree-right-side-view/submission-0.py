# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        nodes = deque()
        ans = []
        nodes.append(root)

        while len(nodes) > 0:
            n = len(nodes)
            for i in range(n):
                currNode = nodes.popleft()
                if i == n-1:
                    ans.append(currNode.val)

                if currNode.left:
                    nodes.append(currNode.left)
                if currNode.right:
                    nodes.append(currNode.right)

        return ans