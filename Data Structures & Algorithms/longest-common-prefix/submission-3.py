class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i,c in enumerate(strs[0]):
            for s in strs[1:len(strs)]:
                if s != "" and i < len(s) and s[i] == c:
                    continue
                else:
                    return strs[0][0:i]
        return strs[0]
        