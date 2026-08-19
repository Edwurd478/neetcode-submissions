from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        currSum = 0
        sums[currSum] += 1
        ans = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if (currSum - k) in sums:
                #print(currSum, currSum - k)
                ans += sums[currSum - k]
            sums[currSum] += 1
        
        return ans
