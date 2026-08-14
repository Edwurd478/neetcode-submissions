class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        arr = nums
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return m
            elif arr[m] > target:
                if m == 0:
                    return 0
                elif arr[m-1] < target:
                    return m
                else:
                    r = m - 1
            else:
                if m == len(nums)-1:
                    return len(nums)
                elif arr[m+1] > target:
                    return m + 1
                else:
                    l = m + 1
            