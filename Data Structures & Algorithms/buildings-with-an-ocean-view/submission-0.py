"""
[4, 4, 4, 4, 4]
[4, 3, 3, 2, 1]
"""
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        psum = [0] * n
        ssum = [0] * n
        result = []

        max_height = 0
        for i in range(n):
            if heights[i] > max_height:
                max_height = heights[i]
                psum[i] = i
            else:
                psum[i] = psum[i-1]
        
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
        #print(psum, ssum)
        return result

