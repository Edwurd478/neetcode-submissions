class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        curr = []
        for a in asteroids:
            if len(curr) == 0:
                curr.append(a)
                continue
            b = curr[-1]
            if a < 0 and b > 0:
                while len(curr) > 0 and b > 0 and abs(a) > abs(b):
                    curr.pop()
                    if len(curr) > 0:
                        b = curr[-1]
                #print(a, b)
                if len(curr) == 0 or b < 0:
                    curr.append(a)
                elif abs(b) == abs(a):
                    curr.pop()
            else:
                curr.append(a)
        
        return curr