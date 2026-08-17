class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower = max(weights)
        upper = sum(weights)

        def simulateLoading(cap: int) -> int:
            numDays = 0
            currWeight = 0
            for w in weights:
                if currWeight + w > cap:
                    numDays += 1
                    currWeight = w
                elif currWeight + w == cap:
                    numDays += 1
                    currWeight = 0
                else:
                    currWeight += w
                
                #print(currWeight, numDays)
            
            return numDays+1 if currWeight > 0 else numDays
        ans = upper
        while lower <= upper:
            mid = (lower + upper) // 2
            #print(mid, simulateLoading(mid))
            if simulateLoading(mid) > days:
                lower = mid + 1
            else:
                ans = mid
                upper = mid - 1
        
        return ans