class Solution:
    def trap(self, height: List[int]) -> int:
        psum = []
        ssum = [-1] * len(height)
        for i, h in enumerate(height):
            if i == 0:
                psum.append(h)
            else:
                psum.append(max(psum[i-1], h))
        
        for i in range(len(height)-1, -1, -1):
            h = height[i]
            if i == len(height)-1:
                ssum[i] = h
            else:
                ssum[i] = max(ssum[i+1], h)
        
        result = 0
        for i, h in enumerate(height):
            tallest_water = min(psum[i], ssum[i])
            result += tallest_water - h
        
        return result