class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        nums.sort()

        def backtrack(idx):
            if idx == len(nums):
                result.append(curr.copy())
                return
            
            curr.append(nums[idx])
            backtrack(idx+1)
            curr.pop()

            while idx < len(nums) - 1 and nums[idx] == nums[idx+1]:
                idx += 1

            backtrack(idx+1)
        
        backtrack(0)

        return result