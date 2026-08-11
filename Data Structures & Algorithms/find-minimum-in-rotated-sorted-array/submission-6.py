class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        lptr, rptr = 0, n-1
        #curr = float("inf")
        while lptr < rptr:
            mid = (rptr + lptr) // 2
            if nums[mid] > nums[rptr]:
                lptr = mid + 1
            else:
                rptr = mid
        
        return nums[lptr]