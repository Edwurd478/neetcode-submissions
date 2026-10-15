class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for s in details:
            age = int(s[-4:-2])
            #print(age)
            if age > 60:
                result += 1
            
        return result