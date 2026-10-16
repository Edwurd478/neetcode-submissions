class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        sum = 0
        targ = min(nums)

        while targ > 0:
            sum += targ % 10
            targ = targ // 10
        
        return 1 - (sum % 2)
