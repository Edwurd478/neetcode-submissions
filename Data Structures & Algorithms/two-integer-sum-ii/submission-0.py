class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr, hptr = 0, len(numbers)-1
        while lptr < hptr:
            if numbers[lptr] + numbers[hptr] < target:
                lptr += 1
            elif numbers[lptr] + numbers[hptr] > target:
                hptr -= 1
            else:
                return [lptr+1, hptr+1]