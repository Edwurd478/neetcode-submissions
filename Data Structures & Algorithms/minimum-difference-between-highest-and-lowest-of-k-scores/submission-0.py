class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        arr = sorted(nums)
        result = float("inf")
        for i in range(k-1, len(arr)):
            result = min(result, arr[i] - arr[i - k + 1])

        return result