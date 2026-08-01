class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if i == 0:
                continue
            ans += abs(ord(s[i])-ord(s[i-1]))
        return ans