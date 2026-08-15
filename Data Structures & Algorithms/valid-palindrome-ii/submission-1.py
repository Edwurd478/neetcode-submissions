class Solution:
    mistakes = 0
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        global mistakes
        while l < r:
            if s[l] != s[r] and self.mistakes == 0:
                self.mistakes = 1
                print(s[:l]+s[l+1:], s[:r]+s[r+1:])
                if self.validPalindrome(s[:l]+s[l+1:]) or self.validPalindrome(s[:r]+s[r+1:]):
                    return True
                else:
                    return False
            elif s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True