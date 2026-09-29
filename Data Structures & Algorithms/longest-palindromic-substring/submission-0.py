class Solution:
    def longestPalindrome(self, s: str) -> str:
        result, result_length = s[0], 1
        n = len(s)

        for i, c in enumerate(s):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r-l+1
                if length > result_length:
                    result_length = length
                    result = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r-l+1
                if length > result_length:
                    result_length = length
                    result = s[l:r+1]
                l -= 1
                r += 1

        return result 