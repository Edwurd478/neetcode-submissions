"""
aaabc -> abaca
a, b, a, c, a

aaabbbcc
a, b, a, b, c, a, b, c

aabc -> abac
aaac -> ""
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        chars = {} #char -> int
        most_frequent = 0
        for c in s:
            chars[c] = chars.get(c, 0) + 1
            most_frequent = max(most_frequent, chars[c])
        
        n = len(s)
        if (n % 2 == 0 and most_frequent > n // 2) or (n % 2 == 1 and most_frequent > n // 2 + 1):
            return ""
        
        result = [None]
        while len(chars) > 0:
            keys = sorted(chars, key=lambda x: -chars[x])
            idx = 0 if keys[0] != result[-1] else 1
            result.append(keys[idx])
            chars[keys[idx]] -= 1
            if chars[keys[idx]] == 0:
                del chars[keys[idx]]
        
        return "".join(result[1:])