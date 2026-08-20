class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                popped = stack.pop()
                ans[popped[1]] = i - popped[1]
            
            stack.append((temperatures[i], i))
        
        return ans

                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        waiting = [(temperatures[0], 0)]
        results = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            #if len(waiting) > 0:
             #   print(temperatures[i], waiting[-1][0])
            while len(waiting) > 0 and temperatures[i] > waiting[-1][0]:
                temp, idx = waiting.pop()
                print(temp, idx)
                results[idx] = i - idx
            waiting.append((temperatures[i], i))
        
        return results
        """