# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = deque()
        nodes.append((root, -float("inf"), float("inf")))

        while len(nodes) > 0:
            for i in range(len(nodes)):
                currNode = nodes.popleft()
                currVal = currNode[0].val
                if currVal < currNode[1] or currVal > currNode[2]:
                    return False
                
                if currNode[0].left:
                    nodes.append((currNode[0].left, currNode[1], min(currNode[2], currVal-1)))
                if currNode[0].right:
                    nodes.append((currNode[0].right, max(currNode[1], currVal+1), currNode[2]))

        return True
