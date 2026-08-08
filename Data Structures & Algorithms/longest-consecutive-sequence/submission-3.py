class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        curr = 1
        ans = -1
        #print(nums)
        for i in range(1, len(nums)):
            #print(nums[i] - nums[i-1], curr)
            if nums[i] - nums[i-1] > 1:
                ans = max(ans, curr)
                curr = 1
            elif nums[i] - nums[i-1] == 1:
                curr += 1
        ans = max(ans, curr)
        return ans