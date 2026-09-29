from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        visited = set()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        while len(queue) > 0:
            r,c = queue.popleft()
            for dir in dirs:
                nr, nc = r+dir[0], c+dir[1]
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr,nc) not in visited and grid[nr][nc] != -1:
                    grid[nr][nc] = grid[r][c] + 1
                    visited.add((nr,nc))
                    queue.append((nr,nc))

        
