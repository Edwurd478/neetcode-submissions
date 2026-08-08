from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1

        arr = sorted(map.items(), key = lambda item: item[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(arr[i][0])
        return ans

"""
hashmap (val, freq)
store frequencies of all values in array
sort by frequency -> get top K values
"""