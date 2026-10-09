class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def split(min_val):
            curr_sweet = 0
            num_pieces = 0
            for s in sweetness:
                curr_sweet += s
                if curr_sweet >= min_val:
                    curr_sweet = 0
                    num_pieces += 1
            return num_pieces >= k+1
        
        l, r = 1, sum(sweetness)
        result = 0
        while l <= r:
            m = (l + r) // 2
            if split(m):
                result = max(result, m)
                l = m+1
            else:
                r = m-1
        
        return result