class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dir in dirs:
                nr, nc = r+dir[0], c+dir[1]
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr,nc) not in visited and board[nr][nc] == word[idx]:
                    visited.add((nr,nc))
                    if dfs(nr, nc, idx+1):
                        return True
                    visited.remove((nr,nc))
            return False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited.add((r,c))
                    if dfs(r, c, 1):
                        return True
                    visited.remove((r,c))

        return False