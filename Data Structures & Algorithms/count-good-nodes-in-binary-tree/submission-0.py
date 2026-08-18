# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodes = deque()
        nodes.append((root, root.val))
        ans = 0

        while len(nodes) > 0:
            for i in range(len(nodes)):
                currNode = nodes.popleft()
                if currNode[1] <= currNode[0].val:
                    ans += 1
                
                if currNode[0].left:
                    nodes.append((currNode[0].left, max(currNode[0].left.val, currNode[1])))
                if currNode[0].right:
                    nodes.append((currNode[0].right, max(currNode[0].right.val, currNode[1])))
        
        return ans