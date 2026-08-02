class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s)-1
        ans = 0
        startCount = False
        while idx >= 0:
            if s[idx] == " " and startCount == True:
                break
            elif s[idx] != " " and startCount == True:
                ans += 1
            elif s[idx] != " " and startCount == False:
                startCount = True
                ans += 1
            idx -= 1
        return ans