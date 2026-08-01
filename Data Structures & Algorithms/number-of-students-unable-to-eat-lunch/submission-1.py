from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        idx = 0
        counter = 0
        while len(queue) > 0 and counter < len(queue) and idx < len(sandwiches):
            if queue[0] != sandwiches[idx]:
                queue.append(queue.popleft())
                counter += 1
            else:
                counter = 0
                queue.popleft()
                idx += 1
        return len(queue)