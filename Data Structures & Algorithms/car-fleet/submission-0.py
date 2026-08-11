class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i], (target-position[i])/speed[i]) for i in range(len(speed))]
        cars.sort()
        ans = len(speed)

        curr = cars.pop()[2]
        while len(cars) > 0:
            time = cars.pop()[2]
            if time <= curr:
                #form fleet
                ans -= 1
            else:
                curr = time
        
        return ans
