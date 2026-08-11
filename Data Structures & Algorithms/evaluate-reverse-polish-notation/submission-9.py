class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                num2, num1 = nums.pop(), nums.pop()
                nums.append(num1 + num2)
            elif tokens[i] == "-":
                num2, num1 = nums.pop(), nums.pop()
                nums.append(num1 - num2)
            elif tokens[i] == "*":
                num2, num1 = nums.pop(), nums.pop()
                nums.append(num1 * num2)
            elif tokens[i] == "/":
                num2, num1 = nums.pop(), nums.pop()
                nums.append(num1 // num2)
                if nums[-1] < 0 and num1 % num2 != 0:
                    nums[-1] += 1
            else:
                nums.append(int(tokens[i]))
        
        return nums[-1]