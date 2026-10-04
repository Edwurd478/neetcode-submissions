class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dir_change = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}
        result = []
        for i in range(n):
            result.append([])
            for j in range(n):
                result[i].append(0)
        
        r, c = 0, 0
        dr, dc = 0, 1
        for num in range(1, n**2 + 1):
            result[r][c] = num
            tr, tc = r+dr, c+dc
            if tr >= 0 and tr < n and tc >= 0 and tc < n and result[tr][tc] == 0:
                r, c = tr, tc
            else:
                #change directions
                dr, dc = dir_change[(dr, dc)]
                r, c = r+dr, c+dc
        
        return result
