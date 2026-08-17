class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currProf = totProf = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                if currProf > 0:
                    totProf += currProf
                currProf = 0
            else:
                currProf += prices[i] - prices[i-1]
        
        if currProf > 0:
            totProf += currProf
        return totProf

        
        """
        assume you are always holding the stock
        every time there is a decrease, sell the stock and buy it IF the cumulative profit for that range is    
        positive (otherwise, assume you never held the stock to begin with)
        every time there is an increase, hold the stock

    
        [7 1 5 3 6 4]
        """