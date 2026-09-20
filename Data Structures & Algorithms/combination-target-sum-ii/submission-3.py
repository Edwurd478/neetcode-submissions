class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        curr_path = []
        def backtrack(idx, curr):
            if curr >= target or idx >= len(candidates):
                if curr == target:
                    result.append(curr_path.copy())
                return
            
            curr_path.append(candidates[idx])
            backtrack(idx+1, curr+candidates[idx])
            curr_path.pop()

            while idx < len(candidates)-1 and candidates[idx] == candidates[idx+1]:
                idx += 1

            backtrack(idx+1, curr)

        backtrack(0, 0)
        return result