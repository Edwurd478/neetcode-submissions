class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if (m > 0 and nums[m] <= nums[m-1]) or (m == 0 and nums[0] <= nums[-1]):
                return nums[m]
            else:
                if nums[m] > nums[-1]:
                    l = m + 1
                else:
                    r = m - 1
            





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        ans = float("inf")
        l, r = 0, len(nums)-1

        while l <= r:
            # "base case" where the portion of the array we're considering is fully sorted
            if nums[r] > nums[l]:
                ans = min(ans, nums[l])
                break

            m = (l + r) // 2
            # test if middle number is the minimum
            ans = min(nums[m], ans)
            if nums[m] > nums[r]: # we are in the left sorted portion (inflection point is to the right of m)
                l = m + 1
            else: # we are in the right sorted portion and see if we can do better than m
                r = m - 1
        
        return ans
        """