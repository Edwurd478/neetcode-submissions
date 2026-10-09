class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq = {}
        num_distinct = 0
        l = 0
        result = 0

        for r in range(len(s)):
            c = s[r]
            if c not in freq or freq[c] == 0:
                num_distinct += 1
            freq[c] = freq.get(c, 0) + 1
            
            while num_distinct > 2:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    num_distinct -= 1
                l += 1
            
            result = max(result, r-l+1)
        
        return result