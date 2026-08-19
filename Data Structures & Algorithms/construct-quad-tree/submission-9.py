"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def constructHelper(x, y, length, currNode):
            currVal = grid[x][y]
            leafFlag = True
           # print(x, y, length)
           # print(grid)
            for i in range(x, x+length):
                for j in range(y, y+length):
                    #print(x, y, grid[x][y], currVal)
                    if grid[i][j] != currVal:
                        leafFlag = False
                        break
                if not leafFlag:
                    break
            #print(leafFlag)
            if leafFlag:
                currNode.isLeaf = True
                currNode.val = currVal
                currNode.topLeft = None
                currNode.topRight = None
                currNode.bottomLeft = None
                currNode.bottomRight = None
            else:
                #print(x,y)
                currNode.val = -1
                currNode.isLeaf = False
                currNode.topLeft = Node()
                currNode.topRight = Node()
                currNode.bottomLeft = Node()
                currNode.bottomRight = Node()
                constructHelper(x, y, length // 2, currNode.topLeft)
                constructHelper(x, y+(length//2), length // 2, currNode.topRight)
                constructHelper(x+(length//2), y, length // 2, currNode.bottomLeft)
                constructHelper(x+(length//2), y+(length//2), length // 2, currNode.bottomRight)
        
        quadTree = Node()
        constructHelper(0, 0, len(grid), quadTree)
        return quadTree