class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for word in words:
            for targ in words:
                if targ == word:
                    continue
                if word in targ:
                    result.add(word)
        
        return list(result)