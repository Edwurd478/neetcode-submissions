from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        mods = [0] * k
        prefix = [0] * n
        
        prefix[0] = nums[0]
        mods[nums[0] % k] += 1

        ans = mods[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
            if prefix[i] % k == 0:
                ans += 1
            ans += mods[prefix[i] % k]
            mods[prefix[i] % k] += 1
       # print(prefix, mods)

        return ans
        
        """
        n = len(nums)
        mods = defaultdict(list)
        prefix = [0] * n
        prefix[0] = nums[0]
        mods[prefix[0] % k].append(0)
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
            mods[prefix[i] % k].append(i)
        print(prefix)
        print(mods)
        
        ans = 0
        for i in range(n):
            currMod = prefix[i] % k
            neededMod = k - currMod if currMod != 0 else 0
            if neededMod in mods:
                for idx in mods[neededMod]:
                    if idx < i:
                        ans += 1
        
        return ans
        """
