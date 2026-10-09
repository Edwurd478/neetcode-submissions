"""
]]][[[

[]][][

[[][]]
"""
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        unmatched = 0

        for c in s:
            if c == "[":
                stack.append(c)
            else:
                if not stack:
                    unmatched += 1
                else:
                    stack.pop()
        
        unmatched += len(stack)
        return unmatched // 4 if unmatched % 4 == 0 else unmatched // 4 + 1