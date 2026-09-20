class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        result = []
        curr = []
        letters = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        def backtrack(idx):
            if idx == len(digits):
                result.append("".join(curr))
                return
            
            for letter in letters[digits[idx]]:
                curr.append(letter)
                backtrack(idx+1)
                curr.pop()

        backtrack(0)
        return result