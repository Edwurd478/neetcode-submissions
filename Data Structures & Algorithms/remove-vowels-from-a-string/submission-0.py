class Solution:
    def removeVowels(self, s: str) -> str:
        to_remove = set()
        for i in range(len(s)):
            c = s[i]
            if c in "aeiou":
                to_remove.add(i)
        
        result = ""
        for i, c in enumerate(s):
            if i not in to_remove:
                result += c
        
        return result
