# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preprocess indices for O(1) searching
        indices = {val: idx for idx, val in enumerate(inorder)}
        n = len(preorder)

        def buildHelper(preIdx1, preIdx2, inIdx1, inIdx2):
            if preIdx1 == preIdx2 or inIdx1 == inIdx2:
                return None
            #print(preIdx1, preIdx2)
            rootVal = preorder[preIdx1]
            rootIdx = indices[rootVal]
            leftLen = rootIdx - inIdx1

            tree = TreeNode(rootVal)
            #print(rootVal, "left", preIdx1+1, preIdx1+1+leftLen, inIdx1, inIdx1+rootIdx)
            tree.left = buildHelper(preIdx1+1, preIdx1+1+leftLen, inIdx1, rootIdx)
            #print(rootVal, "right", preIdx1+1+leftLen, preIdx2, rootIdx+1, inIdx2)
            tree.right = buildHelper(preIdx1+1+leftLen, preIdx2, rootIdx+1, inIdx2)

            return tree
        
        return buildHelper(0, n, 0, n)

