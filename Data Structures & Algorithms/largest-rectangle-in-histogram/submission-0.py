"""
Solution can be O(N), so can do one pass through the array

I notice that a rectangle will always include at least one of the pillars; that is, there will always be a pillar that is the "limiting" height

Why don't we loop through all the pillars and try to calculate the largest rectangle which is limited by that pillar's height?

The boundaries of the largest rectangle will be the first pillar on the left and right that are shorter than the current pillar (we can view boundaries as height 0)

Start by scanning left to right, and keep track of all rectangles that are still "unfinished" (i.e. we haven't found a shorter pillar to the right of it yet)

Once we do find a shorter pillar, we have our right boundary, and can then look backwards to find the left boundary as well. Then we can calculate the area of the rectangle and update our result.
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []  # (index, height)

        for i, height in enumerate(heights):
            right_boundary = i
            start = i
            while stack and stack[-1][1] > height:
                left_boundary, popped_height = stack.pop()
                area = (right_boundary - left_boundary) * popped_height
                result = max(result, area)
                start = left_boundary
            stack.append((start, height))
        
        n = len(heights)
        while stack:
            left_boundary, popped_height = stack.pop()
            area = (n - left_boundary) * popped_height
            result = max(result, area)

        return result
