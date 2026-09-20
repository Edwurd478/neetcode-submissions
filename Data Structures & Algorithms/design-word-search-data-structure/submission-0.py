class TrieNode:
    def __init__(self):
        self.children = {} #char -> TrieNode()
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        
        result = False
        def dfs(idx, curr):
            nonlocal result
            if idx == len(word):
                if curr.is_word:
                    result = True
                return
            
            c = word[idx]
            if c != ".":
                if c not in curr.children:
                    return
                else:
                    dfs(idx+1, curr.children[c])
            else:
                for next_c in curr.children:
                    dfs(idx+1, curr.children[next_c])
        
        dfs(0, self.root)
        return result
