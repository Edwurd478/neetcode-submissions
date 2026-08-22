class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totMod = sum(nums) % p
        if totMod == 0:
            return 0

        n = len(nums)
        mods = {0: -1}
        prefix = [0] * n

        ans = float("inf")
        for i in range(n):
            if nums[i] == totMod:
                return 1

            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] + nums[i]
            
            currMod = prefix[i] % p
            neededMod = (currMod - totMod + p) % p
            #print(prefix[i], currMod, neededMod)
            if neededMod in mods:
                ans = min(ans, i - mods[neededMod])

            mods[currMod] = i
        
        return ans if ans != float("inf") and ans != n else -1