"""
1. Calculate number of satisfied customers without the technique
2. Fixed sliding window of size minutes
    - adjust # of satisfied customers based on how many "flip" from not satisfied to satisfied
"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        num_satisfied = 0
        for c, g in zip(customers, grumpy):
            if g == 0:
                num_satisfied += c

        num_switched = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                num_switched += customers[i]
        result = num_satisfied + num_switched

        r = minutes
        while r < len(customers):
            l = r - minutes + 1
            if grumpy[l-1] == 1:
                num_switched -= customers[l-1]
            if grumpy[r] == 1:
                num_switched += customers[r]
            result = max(result, num_satisfied + num_switched)
            l += 1
            r += 1
        
        return result
