class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        tracker = set()
        tracker.add(nums[0])
        for R in range(1, len(nums)):
            if R - L > k:
                tracker.remove(nums[L])
                L += 1
            
            if nums[R] in tracker:
                return True
            else:
                tracker.add(nums[R])
        
        return False