class Solution:
    def merge(self, nums, left, mid, right):
        l = nums[left:mid]
        r = nums[mid:right]
        i1 = i2 = 0
        idx = left
        
        while i1 < len(l) and i2 < len(r):
            if l[i1] <= r[i2]:
                nums[idx] = l[i1]
                i1 += 1
                idx += 1
            else:
                nums[idx] = r[i2]
                i2 += 1
                idx += 1
        
        while i1 < len(l):
            nums[idx] = l[i1]
            i1 += 1
            idx += 1
        while i2 < len(r):
            nums[idx] = r[i2]
            i2 += 1
            idx += 1
                

    def mergeSort(self, nums, left, right):
        if right - left <= 1:
            return nums
        mid = left + (right-left)//2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid, right)
        self.merge(nums, left, mid, right)
        return nums

    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums))