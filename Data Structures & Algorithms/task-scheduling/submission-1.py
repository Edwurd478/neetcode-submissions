"""
loop by timestamp
keep a min-heap of tasks, sorted by 1. next available timestamp, and 2. frequency of task
at each timestamp, check if the earliest available task can be completed:
    - if yes, complete the task
    - if no, idle
whenever a task is completed, decrease its frequency by 1 and set its next available timestamp to current_timstamp + n + 1
    - but if the task's frequency becomes 0, delete it

[A, A, A, B, C]
heap: [(9, 1, A)]
timestamp = 5

optimization: eliminate looping thru idle timestamps by jumping
"""
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        timestamp = 0
        frequencies = {}
        active = []
        waiting = deque()

        for task in tasks:
            frequencies[task] = frequencies.get(task, 0) + 1
        for task in frequencies:
            active.append((-frequencies[task], task))
        
        heapq.heapify(active)

        while len(waiting) > 0 or len(active) > 0:
            timestamp += 1
            while len(waiting) > 0 and timestamp == waiting[0][0]:
                _, task = waiting.popleft()
                heapq.heappush(active, (-frequencies[task], task))
            if len(active) > 0:
                freq, task = heapq.heappop(active)
                freq += 1
                frequencies[task] -= 1
                if freq < 0:
                    waiting.append((timestamp+n+1, task))
        
        return timestamp


            
