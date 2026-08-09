from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        used = defaultdict(int)
        for i in range(len(nums)):
            target = -nums[i]
            lptr, hptr = 0, len(nums)-1
            while lptr < hptr and lptr != i and hptr != i:
                curr = nums[lptr] + nums[hptr]
                if curr < target:
                    lptr += 1
                elif curr > target:
                    hptr -= 1
                else:
                    candidate = [nums[i],nums[lptr],nums[hptr]]
                    candidate.sort()
                    triplet = (candidate[0], candidate[1], candidate[2])
                    if triplet not in used:
                        used[triplet] = 1
                        ans.append(candidate)
                    lptr += 1
                    hptr -= 1
        return ans