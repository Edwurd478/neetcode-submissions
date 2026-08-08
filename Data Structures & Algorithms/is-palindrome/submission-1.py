class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1. filter the string
        filteredStr = []
        for c in s:
            if (c >= "A" and c <= "Z") or (c >= "a" and c <= "z") or (c >= "0" and c <= "9"):
                filteredStr.append(c)
        
        newStr = "".join(filteredStr)
        newStr = newStr.lower()

        #2. Test if palindrome (2 pointers)
        startPtr, endPtr = 0, len(newStr)-1
        while startPtr < endPtr:
            if newStr[startPtr] != newStr[endPtr]:
                return False
            else:
                startPtr += 1
                endPtr -= 1
        
        return True
