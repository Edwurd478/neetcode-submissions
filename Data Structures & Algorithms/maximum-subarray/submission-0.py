class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")
        currSum = nums[0]

        for i in range(1, len(nums)):
            ans = max(ans, currSum)
            if currSum < 0:
                currSum = nums[i]
            else:
                currSum += nums[i]
        
        return max(ans, currSum)