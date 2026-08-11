class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float("inf")
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[r] > nums[l]:
                ans = min(ans, nums[l])
                break

            m = (l + r) // 2
            ans = min(nums[m], ans)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return ans
