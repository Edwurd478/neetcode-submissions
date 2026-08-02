# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs, start, middle, end):
        half1 = pairs[start:middle]
        half2 = pairs[middle:end]

        idx1 = idx2 = 0
        pairsIdx = start
        while idx1 < len(half1) and idx2 < len(half2):
            if half1[idx1].key <= half2[idx2].key:
                pairs[pairsIdx] = half1[idx1]
                idx1 += 1
            else:
                pairs[pairsIdx] = half2[idx2]
                idx2 += 1
            pairsIdx += 1
        
        while idx1 < len(half1):
            pairs[pairsIdx] = half1[idx1]
            idx1 += 1
            pairsIdx += 1
        while idx2 < len(half2):
            pairs[pairsIdx] = half2[idx2]
            idx2 += 1
            pairsIdx += 1
    
    def myMergeSort(self, pairs: List[Pair], start, end) -> List[Pair]:
        if end-start <= 1:
            return pairs
        middle = start + ((end - start) // 2)
        #print(start, end, middle)
        self.myMergeSort(pairs, start, middle)
        self.myMergeSort(pairs, middle, end)

        self.merge(pairs, start, middle, end)
        return pairs
    
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.myMergeSort(pairs, 0, len(pairs))