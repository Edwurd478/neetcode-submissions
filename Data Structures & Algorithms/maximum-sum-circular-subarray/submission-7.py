class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = minSum = currSumMax = currSumMin = nums[0]

        for i in range(1, len(nums)):
            if currSumMax < 0:
                currSumMax = 0
            if currSumMin > 0:
                currSumMin = 0
            currSumMax += nums[i]
            currSumMin += nums[i]
            maxSum = max(maxSum, currSumMax)
            minSum = min(minSum, currSumMin)
        
        return max(maxSum, sum(nums) - minSum) if minSum != sum(nums) else maxSum
        
        """
        nums.extend(nums[:])
        L = 0
        ans = nums[L]
        currSum = nums[L]
        for R in range(1, len(nums)):
            print(L, R, currSum)
            if R - L >= (len(nums) // 2):
                #print("max length exceeded")
                currSum -= nums[L]
                L += 1
            ans = max(ans, currSum)
            if currSum < 0:
                currSum = 0
                L = R
            
            currSum += nums[R]
        
        return max(ans, currSum)
        """