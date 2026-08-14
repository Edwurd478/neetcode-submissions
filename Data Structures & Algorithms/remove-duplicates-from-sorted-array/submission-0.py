class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNums = set()
        curr = 0
        for i in range(len(nums)):
            if nums[i] not in uniqueNums:
                uniqueNums.add(nums[i])
                nums[curr] = nums[i]
                curr += 1
        
        return curr