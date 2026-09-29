from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        result = 0
        num_bananas = 0
        num_rotten = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    num_bananas += 1
                    if grid[r][c] == 2:
                        num_rotten += 1
                        queue.append((r,c))
        
        while len(queue) > 0:
            success = False
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dir in dirs:
                    nr, nc = r+dir[0], c+dir[1]
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        success = True
                        num_rotten += 1
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
            if success:
                result += 1
        
        return result if num_rotten == num_bananas else -1
