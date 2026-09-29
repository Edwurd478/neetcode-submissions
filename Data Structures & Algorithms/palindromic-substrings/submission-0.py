class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)
        for i, c in enumerate(s):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
        
        return result