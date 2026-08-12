from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        ans = 0
        chars = defaultdict(int)
        L = 0
        
        chars[s[L]] = 0
        for R in range(1, len(s)):
            if s[R] in chars and chars[s[R]] >= L:
                #print(L, R)
                ans = max(ans, R-L)
                #print(s[L:R], chars[s[R]]+1, s[chars[s[R]]+1])
                L = chars[s[R]] + 1
            chars[s[R]] = R
        return max(ans, len(s)-L)
