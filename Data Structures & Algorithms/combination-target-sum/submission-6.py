class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = 0
        curr_path= []
        result = []
        nums.sort()

        def backtrack(idx):
            nonlocal curr
            if curr >= target:
                if curr == target:
                    result.append(curr_path.copy())
                return
            
            for i in range(idx, len(nums)):
                num = nums[i]
                curr += num
                curr_path.append(num)
                backtrack(i)
                curr -= num
                curr_path.pop()
        
        backtrack(0)
        return result
