class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        letters = set()
        for c in source:
            letters.add(c)
        
        idx = 0
        result = 1
        for c in target:
            if c not in letters:
                return -1
            if idx == len(source):
                idx = 0
                result += 1
            while source[idx] != c:
                idx += 1
                if idx == len(source):
                    idx = 0
                    result += 1
            idx += 1
        
        return result
        