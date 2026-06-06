class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for n in nums:
            if n != val:
                n, nums[idx] = nums[idx], n
                idx += 1
        return idx