class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 2:
            return 0

        steps = [0] * (n+1)
        for i in range(2, n+1):
            steps[i] = min(steps[i-1] + cost[i-1], steps[i-2] + cost[i-2])
        
        return steps[n]
