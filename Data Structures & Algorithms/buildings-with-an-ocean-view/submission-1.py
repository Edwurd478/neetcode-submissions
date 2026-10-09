"""
[4, 4, 4, 4, 4]
[4, 3, 3, 2, 1]
"""
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ssum = [0] * n
        result = []

        max_height = 0
        for i in range(n-1, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                ssum[i] = i
            else:
                ssum[i] = ssum[i+1]
        
        for i in range(n):
            if ssum[i] == i:
                result.append(i)

        return result

