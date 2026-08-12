class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        tot = sum(arr[:k])
        sumThreshold = threshold * k
        ans = 1 if tot >= sumThreshold else 0

        for R in range(k, len(arr)):
            tot -= arr[L]
            L += 1
            tot += arr[R]
            if tot >= sumThreshold:
                ans += 1
        
        return ans