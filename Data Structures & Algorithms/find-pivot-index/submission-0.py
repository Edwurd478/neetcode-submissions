class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        postfix = [0] * len(nums)
        postfix[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] + nums[i]
        
        for i in range(len(nums)):
            presum = prefix[i-1] if i > 0 else 0
            postsum = postfix[i+1] if i < len(nums)-1 else 0
            if presum == postsum:
                return i
        
        return -1