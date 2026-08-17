class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        # step 1: find the pivot (O(logn))
        """
        pivot = -1
        l, r = 0, n-1
        while l <= r:
        
            #if nums[l] < nums[r]:
             #   pivot = l
              #  break
            
            m = (l + r) // 2
            #print(l, r, m)
            if m > 0 and nums[m] < nums[m-1]:
                pivot = m
                break

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
            
            pivot = m


        print(pivot)
        """
        pivot = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                pivot = i
                break

        # step 2: binary search (O(logn))
        
        l, r = 0, n-1
        while l <= r:
            m = (l + r) // 2
            correctElement = nums[(pivot + m) % n]
            if correctElement == target:
                return True
            elif correctElement < target:
                l = m + 1
            else:
                r = m - 1
        
        return False


        # space: O(1)