class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(9):
            mySet = set()
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num in mySet:
                        return False
                    else:
                        mySet.add(num)

        #cols
        for i in range(9):
            mySet = set()
            for j in range(9):
                num = board[j][i]
                if num != ".":
                    if num in mySet:
                        return False
                    else:
                        mySet.add(num)

        #grids
        startPositions = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for startI, startJ in startPositions:
            mySet = set()
            for i in range(startI, startI+3):
                for j in range(startJ, startJ+3):
                    num = board[j][i]
                    if num != ".":
                        if num in mySet:
                            return False
                        else:
                            mySet.add(num)
        
        return True