from collections import defaultdict
class AutocompleteSystem:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_sentence = False
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.frequencies = defaultdict(int)
        self.root = self.TrieNode()
        self.new_input = []
        for sentence, frequency in zip(sentences, times):
            self.frequencies[sentence] = frequency
            curr = self.root
            for c in sentence:
                if c not in curr.children:
                    curr.children[c] = self.TrieNode()
                curr = curr.children[c]
            curr.is_sentence = True

    def input(self, c: str) -> List[str]:
        curr = self.root
        if c == "#":
            for char in self.new_input:
                if char not in curr.children:
                    curr.children[char] = self.TrieNode()
                curr = curr.children[char]
            curr.is_sentence = True
            self.frequencies["".join(self.new_input)] += 1 
            self.new_input = []
            return []
        
        result = []
        self.new_input.append(c)
        
        for char in self.new_input:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        def dfs(node: self.TrieNode, curr_sentence: list[str]) -> None:
            if node.is_sentence:
                result.append("".join(curr_sentence))
            for char in node.children:
                curr_sentence.append(char)
                dfs(node.children[char], curr_sentence)
                curr_sentence.pop()

        dfs(curr, self.new_input.copy())
        result.sort(key = lambda x: (-self.frequencies[x], x))
        return result[:min(3, len(result))]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
