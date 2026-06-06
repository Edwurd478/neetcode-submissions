class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        ans = []
        for i, n in enumerate(nums):
            if n in myMap:
                ans.append(i)
                ans.append(myMap[n])
                ans.sort()
                return ans
            myMap[target-n] = i
        