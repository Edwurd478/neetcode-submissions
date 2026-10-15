class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        sum = 0
        result = 0
        for w in weight:
            sum += w
            if sum > 5000:
                return result
            result += 1
        return result