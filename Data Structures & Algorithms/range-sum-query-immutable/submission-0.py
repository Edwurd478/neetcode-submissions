class NumArray:

    def __init__(self, nums: List[int]):
        self.psums = []
        for n in nums:
            if len(self.psums) > 0:
                self.psums.append(self.psums[-1] + n)
            else:
                self.psums.append(n)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.psums[right]
        else:
            return self.psums[right] - self.psums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)