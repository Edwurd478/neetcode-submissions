class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [-1] * n

        def dfs(i, end):
            if i >= end:
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dfs(i+1, end), nums[i]+dfs(i+2, end))
            return memo[i]
        
        first = dfs(0, n-1)
        memo = [-1] * n
        second = dfs(1, n)
        return max(first, second)