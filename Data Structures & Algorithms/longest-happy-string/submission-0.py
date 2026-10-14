"""
Initial strategy:
do aa then bb then cc until limits are reached
a = 3, b = 3, c = 7
aabbccabcc
abccabccaccbc

Smarter strategy:
try placing the "most abundant" character first, unless it breaks a rule
a = 1, b = 2, c = 2
ccaccbcabcabc
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""
        chars = [[a, "a"], [b, "b"], [c, "c"]]

        def can_place(ch, idx):
            nonlocal result
            nonlocal chars

            if len(result) < 2:
                return True
            if chars[idx][0] <= 0:
                return False
            if result[-1] == ch and result[-2] == ch:
                return False
            return True

        while True:
            chars.sort(reverse=True)
            if chars[0][0] == 0:
                break

            i = 0
            while i < 3 and not can_place(chars[i][1], i):
                i += 1
            if i == 3:
                break
            
            chars[i][0] -= 1
            result += chars[i][1]
        
        return result



        