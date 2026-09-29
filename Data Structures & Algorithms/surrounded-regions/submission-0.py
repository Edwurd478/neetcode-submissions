from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        queue = deque()
        visited = set()

        for r in range(rows):
            for c in (0, cols-1):
                if board[r][c] == "O" and (r,c) not in visited:
                    queue.append((r,c))
                    visited.add((r,c))
        for c in range(cols):
            for r in (0, rows-1):
                if board[r][c] == "O" and (r,c) not in visited:
                    queue.append((r,c))
                    visited.add((r,c))

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while len(queue) > 0:
            r, c = queue.popleft()
            for dir in dirs:
                nr, nc = r+dir[0], c+dir[1]
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc) not in visited and board[nr][nc] == "O":
                    queue.append((nr,nc))
                    visited.add((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited:
                    board[r][c] = "X"
                