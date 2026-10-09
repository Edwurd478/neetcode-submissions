"""
fixed sliding window of size k
count the number of existing white blocks in each window, find the min
"""
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        num_white = 0
        for i in range(k):
            if blocks[i] == "W":
                num_white += 1
        
        result = num_white
        l, r = 1, k
        while r < len(blocks):
            if blocks[l-1] == "W":
                num_white -= 1
            if blocks[r] == "W":
                num_white += 1
            result = min(result, num_white)
            l += 1
            r += 1

        return result
        