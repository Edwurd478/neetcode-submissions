class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for i in range(len(tokens)):
            #print(stack)
            if tokens[i] not in operations:
                stack.append(int(tokens[i]))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if tokens[i] == "+":
                    stack.append(op1 + op2)
                elif tokens[i] == "-":
                    stack.append(op1 - op2)
                elif tokens[i] == "*":
                    stack.append(op1 * op2)
                else:
                    quotient = op1 // op2
                    if quotient < 0 and op1 % op2 != 0:
                        quotient += 1
                    stack.append(quotient)
        
        return stack[-1]

        












        
        """
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
        """