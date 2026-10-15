class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        idx = 0
        i = 0
        result = 0
        g.sort()
        s.sort()
        while idx < len(s) and i < len(g):
            if s[idx] >= g[i]:
                result += 1
                i += 1
            idx += 1

        return result