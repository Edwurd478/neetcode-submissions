class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        #get all start and end positions, sorted
        #add to stack, pop when you see an end position, keep track of size of stack

        positions = []
        for light in lights:
            start, end = light[0] - light[1], light[0] + light[1]
            positions.append((start, 0))
            positions.append((end, 1))
        
        positions.sort()

        stack = []
        max_size = -1
        brightest_position = None

        for position in positions:
            pos, label = position
            if label == 0:
                stack.append(pos)
                if len(stack) > max_size:
                    max_size = len(stack)
                    brightest_position = pos
            else:
                stack.pop()
        
        return brightest_position