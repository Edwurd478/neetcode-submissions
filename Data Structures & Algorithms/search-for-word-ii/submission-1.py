class TrieNode:
    def __init__(self):
        self.children = {} #char -> TrieNode
        self.is_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        rows, cols = len(board), len(board[0])
        #build prefix tree for all words
        root = TrieNode()
        for word in words:
            curr = root
            for i, c in enumerate(word):
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                if i == len(word) - 1:
                    curr.is_word = True
        #for every cell, dfs with that as the starting letter, add to results
        #array when we find a word
        visited = set()
        def dfs(r: int, c: int, node: TrieNode, word: str) -> None:
            if node.is_word:
                result.add(word)
                
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dir in dirs:
                nr, nc = r+dir[0], c+dir[1]
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc) not in visited and board[nr][nc] in node.children:
                    visited.add((nr,nc))
                    #print(f"added {(nr,nc)} to visited when word is {word}")
                    dfs(nr, nc, node.children[board[nr][nc]], word+board[nr][nc])
                    #print(f"removed {(nr,nc)} from visited when word is {word}")
                    visited.remove((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    visited.add((r,c))
                    dfs(r, c, root.children[board[r][c]], board[r][c])
                    visited.remove((r,c))
        
        return list(result)

"""
o a a n
e t a e
i h k r
i f l v
"""







