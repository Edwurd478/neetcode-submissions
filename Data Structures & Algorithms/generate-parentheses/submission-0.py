class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr = []
        def backtrack(num_paren, stack):
            if num_paren == n and not stack:
                result.append("".join(curr))
                return
            
            if num_paren < n:
                curr.append("(")
                stack.append("(")
                backtrack(num_paren+1, stack)
                stack.pop()
                curr.pop()

            if stack:
                curr.append(")")
                stack.pop()
                backtrack(num_paren, stack)
                curr.pop()
                stack.append("(")
        
        backtrack(0, [])

        return result