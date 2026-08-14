class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0
        maxLen = 1
        def canAdd(idx):
            if idx == L:
                return True
            if idx == L+1:
                return arr[idx] != arr[L]

            if arr[idx] > arr[idx-1]:
                return True if arr[idx-1] < arr[idx-2] else False
            elif arr[idx] < arr[idx-1]:
                return True if arr[idx-1] > arr[idx-2] else False

            return False

        for R in range(len(arr)):
            if canAdd(R):
                maxLen = max(maxLen, R-L+1)
            else:
                while not canAdd(R):
                    L += 1

        return maxLen 
