class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        [0, 1, 3, 7]             
                     |
        [1, 1, 1, 0, 0, 1, 0, 1, 0]
        """
        
        n = len(boxes)
        prefix = [0] * n
        postfix = [0] * n
        totalOnes = 0 if boxes[0] == "0" else 1

        for i in range(1, n):
            prefix[i] = prefix[i-1] + totalOnes
            if boxes[i] == "1":
                totalOnes += 1
            
        totalOnes = 0 if boxes[-1] == "0" else 1    
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] + totalOnes
            if boxes[i] == "1":
                totalOnes += 1
        
        ans = [prefix[i] + postfix[i] for i in range(n)]
        return ans