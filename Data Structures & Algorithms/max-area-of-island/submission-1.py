from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                
                area = 0
                queue.append((r,c))
                grid[r][c] = 0
                while len(queue) > 0:
                    cr, cc = queue.pop()
                    area += 1
                    for dir in dirs:
                        nr, nc = cr+dir[0], cc+dir[1]
                        if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                            queue.append((nr,nc))
                            grid[nr][nc] = 0
                result = max(result, area)
        
        return result


