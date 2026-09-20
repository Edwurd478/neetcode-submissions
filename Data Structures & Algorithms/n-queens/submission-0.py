class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        curr = []

        def is_valid(square): #checks diagonals
            i, j = square
            #top right
            i -= 1
            j += 1
            while i >= 0 and j < n:
                if curr[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            i, j = square
            #top left
            i -= 1
            j -= 1
            while i >= 0 and j >= 0:
                if curr[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            return True
        
        def backtrack(row, occupied):
            if row == n:
                result.append(curr.copy())
                return
            
            for col in range(n):
                if col not in occupied and is_valid((row, col)):
                    placement = "."*col + "Q" + "."*(n-col-1)
                    curr.append(placement)
                    occupied.add(col)
                    backtrack(row+1, occupied)
                    occupied.remove(col)
                    curr.pop()
                
        backtrack(0, set())
        return result
        