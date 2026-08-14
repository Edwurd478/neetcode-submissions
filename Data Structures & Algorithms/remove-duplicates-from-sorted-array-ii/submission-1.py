class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0
        for i in range(len(nums)):
            if curr < 2 or nums[curr-2] != nums[i]:
                nums[curr] = nums[i]
                curr += 1
        
        return curr