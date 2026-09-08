"""
1 2
3 4

1 3
2 4
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        #transpose
        for r in range(rows):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        #reverse each row
        for r in range(rows):
            matrix[r] = matrix[r][::-1]