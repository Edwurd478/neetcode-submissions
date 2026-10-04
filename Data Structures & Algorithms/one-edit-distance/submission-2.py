"""
length of S and T can be at most 1 apart
if same:
    - check # of mismatches to be exactly 1
if 1 apart:
    - loop thru longer string, match with shorter string
    - if mismatch, assume that is the odd one out and skip that char
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) >= 2:
            return False
        
        if len(s) == len(t):
            flag = False
            for i in range(len(s)):
                if s[i] != t[i]:
                    if flag:
                        return False
                    else:
                        flag = True
            return flag
        else:
            n = None
            longer = None
            shorter = None
            if len(s) > len(t):
                n = len(s)
                longer = s
                shorter = t
            else:
                n = len(t)
                longer = t
                shorter = s
            
            sptr, lptr = 0, 0
            flag = False
            while lptr < n:
                if sptr >= len(shorter) or shorter[sptr] != longer[lptr]:
                    if flag:
                        return False
                    else:
                        flag = True
                        lptr += 1
                else:
                    lptr += 1
                    sptr += 1
            return True

