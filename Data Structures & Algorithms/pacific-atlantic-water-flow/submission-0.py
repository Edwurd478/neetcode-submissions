from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = heights
        reachable = {} #(x, y) -> ['p', 'a']
        queue = deque() #((x, y), 'p')
        rows, cols = len(heights), len(heights[0])
        visited_p = set()
        visited_a = set()

        for r in range(rows):
            for c in (0, cols-1):
                if c == 0 or r == 0:
                    if (r,c) not in reachable:
                        reachable[(r,c)] = set()
                    reachable[(r,c)].add("p")
                    queue.append((r, c, "p"))
                    visited_p.add((r,c))
                if c == cols-1 or r == rows-1:
                    if (r,c) not in reachable:
                        reachable[(r,c)] = set()
                    reachable[(r,c)].add("a")
                    queue.append((r, c, "a"))
                    visited_a.add((r,c))
        for r in (0, rows-1):
            for c in range(cols):
                if c == 0 or r == 0:
                    if (r,c) not in reachable:
                        reachable[(r,c)] = set()
                    reachable[(r,c)].add("p")
                    queue.append((r, c, "p"))
                    visited_p.add((r,c))
                if c == cols-1 or r == rows-1:
                    if (r,c) not in reachable:
                        reachable[(r,c)] = set()
                    reachable[(r,c)].add("a")
                    queue.append((r, c, "a"))
                    visited_a.add((r,c))
        #print(visited_p, visited_a, queue, reachable)
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        to_visit = {"p": visited_p, "a": visited_a}
        while len(queue) > 0:
            r, c, label = queue.popleft()
            visited = to_visit[label]
            for dir in dirs:
                nr, nc = r+dir[0], c+dir[1]
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr,nc) not in visited and grid[nr][nc] >= grid[r][c]:
                    visited.add((nr,nc))
                    queue.append((nr,nc,label))
                    if (nr,nc) not in reachable:
                        reachable[(nr,nc)] = set()
                    reachable[(nr,nc)].add(label)

        result = []
        for cell in reachable:
            if len(reachable[cell]) == 2:
                result.append(cell)
        return result



