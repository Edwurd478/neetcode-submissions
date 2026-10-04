"""
1. reverse the entire string
2. use 2 pointers, detect whenever the right pointer reaches a space or end of str, reverse all characters between the pointers
"""
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s.reverse()
        l, r = 0, 0
        while r < len(s):
            r += 1
            if r == len(s) or s[r] == " ":
                tmpl, tmpr = l, r-1
                while tmpr > tmpl:
                    s[tmpl], s[tmpr] = s[tmpr], s[tmpl]
                    tmpr -= 1
                    tmpl += 1
                r += 1
                l = r
            
        