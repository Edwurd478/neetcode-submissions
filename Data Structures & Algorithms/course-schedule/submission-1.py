class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        blocked = [0] * numCourses
        unlocks = {}

        for prereq in prerequisites:
            first, second = prereq[1], prereq[0]
            blocked[second] += 1
            if first not in unlocks:
                unlocks[first] = []
            unlocks[first].append(second)
        
        taken_courses = 0
        while True:
            added = False
            for course in range(numCourses):
                if blocked[course] == 0:
                    added = True
                    taken_courses += 1
                    blocked[course] -= 1
                    if course in unlocks:
                        for unlocked in unlocks[course]:
                            blocked[unlocked] -= 1
            if not added:
                break
        
        return taken_courses == numCourses