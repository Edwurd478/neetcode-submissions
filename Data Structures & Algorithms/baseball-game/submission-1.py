class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == "+":
                scores.append(scores[-1] + scores[-2])
            elif op == "D":
                scores.append(2*scores[-1])
            elif op == "C":
                scores.pop()
            else:
                scores.append(int(op))

        ans = 0
        for n in scores:
            ans += n
        return ans