class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        openclose = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c == "(" or c == "[" or c == "{":
                brackets.append(c)
            elif len(brackets) == 0:
                return False
            else:
                if openclose[c] != brackets.pop():
                    return False
        return len(brackets) == 0