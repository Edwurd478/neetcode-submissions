class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        neighbors = {}
        for pair in similarPairs:
            a, b = pair
            if a not in neighbors:
                neighbors[a] = set()
            if b not in neighbors:
                neighbors[b] = set()
            neighbors[a].add(b)
            neighbors[b].add(a)

        for word in sentence1:
            if word not in neighbors:
                neighbors[word] = set()
            neighbors[word].add(word)
        
        for word in sentence2:
            if word not in neighbors:
                neighbors[word] = set()
            neighbors[word].add(word)

        for word1, word2 in zip(sentence1, sentence2):
            if word2 not in neighbors[word1]:
                return False
        return True

