class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        result = -1
        nums.sort()
        
        for i, num in enumerate(nums):
            before, after = i-1, i+1
            if (before < 0 or nums[before] != num) and (after >= len(nums) or nums[after] != num):
                result = num
        
        return result