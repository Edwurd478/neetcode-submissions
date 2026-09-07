class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        blocked = [0] * numCourses
        unlocks = {} #course -> list[int]

        for pairing in prerequisites:
            second, first = pairing
            if first not in unlocks:
                unlocks[first] = []
            unlocks[first].append(second)
            blocked[second] += 1
        
        result = []
        while True:
            added = False
            for i in range(len(blocked)):
                if blocked[i] == 0:
                    result.append(i)
                    blocked[i] -= 1
                    added = True

                    if i in unlocks:
                        for course in unlocks[i]:
                            blocked[course] -= 1
            if not added:
                break
        
        return result if len(result) == numCourses else []
                

