class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #bucket sort
        """
        Do not return anything, modify nums in-place instead.
        """

        colors = [0] * (max(nums)+1)
        for n in nums:
            colors[n] += 1
        
        idx = 0
        for i, c in enumerate(colors):
            for _ in range(c):
                nums[idx] = i
                idx += 1
        