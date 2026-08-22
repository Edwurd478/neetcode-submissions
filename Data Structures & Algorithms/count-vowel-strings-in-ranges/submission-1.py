class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ["a", "e", "i", "o", "u"]
        n = len(words)
        prefix = [0] * n

        prefix[0] = 1 if (words[0][0] in vowels and words[0][-1] in vowels) else 0
        for i in range(1, n):
            prefix[i] = prefix[i-1]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i] += 1
        
        ans = []
        for query in queries:
            left, right = query
            if left == 0:
               ans.append(prefix[right])
            else:
                ans.append(prefix[right] - prefix[left-1])
        
        return ans