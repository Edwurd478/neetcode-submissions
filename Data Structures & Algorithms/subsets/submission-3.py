class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def getPermutations(currPermutation, currNums):
            #print(currPermutation, currNums)
            if len(currNums) == 0:
                ans.append(currPermutation[:])
                return
            
            getPermutations(currPermutation, currNums[1:])
            currPermutation.append(currNums[0])
            getPermutations(currPermutation, currNums[1:])
            currPermutation.pop()
        
        getPermutations([], nums)
        return ans