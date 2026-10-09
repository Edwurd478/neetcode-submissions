class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #first_zero = nums[0] == 0
        #last_zero = nums[len(nums)-1] == 0
        result = 1
        curr_ones = 0
        counts = []
        for num in nums:
            if num == 1:
                curr_ones += 1
            else:
                counts.append(curr_ones)
                curr_ones = 0
        counts.append(curr_ones)
        if len(counts) == 1:
            return counts[0]
        for i in range(len(counts)-1):
            result = max(result, counts[i]+counts[i+1]+1)
        return result