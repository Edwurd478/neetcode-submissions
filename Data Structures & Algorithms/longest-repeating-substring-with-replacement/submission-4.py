from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        ans = 0
        for i in range(26):
            test = chr(ord("A") + i)
            L = 0
            currDiff = 0 if s[L] == test else 1
            for R in range(1, len(s)):
                if s[R] != test:
                    currDiff += 1
                while currDiff > k:
                    if s[L] != test:
                        currDiff -= 1
                    L += 1
                ans = max(ans, R-L+1)
        
        return ans

        """
        ans = 0
        for i in range(26):
            differences = deque()
            test = chr(ord("A") + i)
            L = 0
            if s[L] != test:
                differences.append(0)
            
            for R in range(1, len(s)):
                if s[R] != test:
                    differences.append(R)
                if len(differences) > k:
                    ans = max(ans, R-L)
                    curr = differences.popleft()
                    L = differences[0] if len(differences) > 0 else curr+1

            ans = max(ans, len(s) - L)

        return ans
        """