class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        freq = {}
        num_distinct = 0
        l = 0
        result = 0
        for r in range(len(s)):
            c = s[r]
            if c not in freq:
                freq[c] = 0
                num_distinct += 1
            freq[c] += 1

            while num_distinct > k:
                to_remove = s[l]
                freq[to_remove] -= 1
                if freq[to_remove] == 0:
                    del freq[to_remove]
                    num_distinct -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result