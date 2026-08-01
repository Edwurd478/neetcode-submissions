class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for c in t:
            #print(c, idx, s[idx])
            if idx == len(s):
                break
            if c == s[idx]:
                idx += 1
        return idx == len(s)
