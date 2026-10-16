class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = set()
        for a in arr:
            nums.add(a)
        
        result = 0
        for num in arr:
            if num+1 in nums:
                result += 1
        
        return result