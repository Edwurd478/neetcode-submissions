class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        L = 0
        currSum = 0
        for R in range(len(nums)):
            currSum += nums[R]
            while currSum >= target:
                minLen = min(minLen, R-L+1)
                currSum -= nums[L]
                L += 1
        
        return minLen if minLen != float("inf") else 0