class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def at_most(n: int) -> int:
            freq = {}
            l = 0
            count = 0
            for r in range(len(nums)):
                freq[nums[r]] = freq.get(nums[r], 0) + 1
                
                while len(freq) > n:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                
                count += r - l + 1
            return count
        
        return at_most(k) - at_most(k-1)
        