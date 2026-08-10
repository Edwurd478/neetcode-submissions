class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lptr, rptr = 0, len(heights)-1
        area = -1
        while lptr < rptr:
            if heights[lptr] < heights[rptr]:
                area = max(area, heights[lptr] * (rptr - lptr))
                lptr += 1
            else:
                area = max(area, heights[rptr] * (rptr - lptr))
                rptr -= 1
        
        return area