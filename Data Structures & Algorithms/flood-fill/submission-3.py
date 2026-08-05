from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c = image[sr][sc]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        queue = deque()
        rows, cols = len(image), len(image[0])
        visited = [[False]*cols for _ in range(rows)]
        queue.append((sr,sc))

        while len(queue) > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                image[i][j] = color
                visited[i][j] = True
                for dr, dc in directions:
                    nr, nc = i+dr, j+dc
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and image[nr][nc] == c and not visited[nr][nc]:
                        queue.append((nr,nc))

        return image
