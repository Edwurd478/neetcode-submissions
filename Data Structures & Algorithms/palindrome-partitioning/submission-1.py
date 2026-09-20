class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        curr = []

        def check_palindrome(cands):
            for cand in cands:
                i, n = 0, len(cand)
                while i <= n // 2:
                    if cand[i] != cand[n-1-i]:
                        return False
                    i += 1
            return True
        
        def is_palindrome(test_str):
            i, n = 0, len(test_str)
            while i <= n // 2:
                if test_str[i] != test_str[n-1-i]:
                    return False
                i += 1
            return True

        def backtrack(prev, idx):
            if idx == len(s):
                if len("".join(curr)) == len(s):
                    result.append(curr.copy())
                return
            
            substr = s[prev:idx+1]
            if is_palindrome(substr):
                curr.append(s[prev:idx+1])
                backtrack(idx+1, idx+1)
                curr.pop()
            backtrack(prev, idx+1)

        backtrack(0, 0)
        return result