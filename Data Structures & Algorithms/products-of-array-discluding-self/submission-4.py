class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes, suffixes = [1] * n, [1] * n
        for i in range(1, n):
            prefixes[i] = prefixes[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i+1]
        print(prefixes, suffixes)
        return [prefixes[i] * suffixes[i] for i in range(n)]