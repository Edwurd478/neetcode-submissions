class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        result = 1
        num_zeros = 1 if nums[0] == 0 else 0

        for r in range(1, len(nums)):
            if nums[r] == 0:
                num_zeros += 1
            while num_zeros > 1:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            
            result = max(result, r-l+1)
        
        return result