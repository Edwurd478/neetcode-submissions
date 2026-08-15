class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        counter = 0
        newWord = []
        while p1 < len(word1) and p2 < len(word2):
            if counter % 2 == 0:
                newWord.append(word1[p1])
                p1 += 1
            else:
                newWord.append(word2[p2])
                p2 += 1

            counter += 1
        
        while p1 < len(word1):
            newWord.append(word1[p1])
            p1 += 1
        while p2 < len(word2):
            newWord.append(word2[p2])
            p2 += 1       
        return "".join(newWord)