from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        numIslands = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    queue.append((i,j))
                    while len(queue) > 0:
                        cr, cc = queue.popleft()
                        grid[cr][cc] = "0"
                        for dr, dc in directions:
                            nr, nc = cr+dr, cc+dc
                            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nr,nc))
                    numIslands += 1
        
        return numIslands