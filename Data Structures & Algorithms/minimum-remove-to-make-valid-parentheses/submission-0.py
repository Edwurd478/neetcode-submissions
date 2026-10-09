class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        result = []

        for i, c in enumerate(s):
            if c != ")" and c != "(":
                continue
            
            if c == "(":
                stack.append(i)
            else:
                if not stack:
                    to_remove.add(i)
                else:
                    stack.pop()
        
        for remaining in stack:
            to_remove.add(remaining)
        
        for i, c in enumerate(s):
            if i not in to_remove:
                result.append(c)
        return "".join(result)
        
