class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        curr = []
        def backtrack(nums_left):
            if not nums_left:
                result.append(curr.copy())
                return
            
            for num in nums_left.copy():
                #print(curr, num, nums_left)
                curr.append(num)
                nums_left.remove(num)
                backtrack(nums_left)
                nums_left.add(num)
                curr.pop()
        
        backtrack(set(nums))
        return result
        