class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isnumeric() or len(i)>1:
                stack.append(int(i))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                print(stack, num1, num2)
                if i == "+":
                    stack.append(num1+num2)
                elif i == "-":
                    stack.append(num1-num2)
                elif i == "*":
                    stack.append(int(num1*num2))
                else:
                    stack.append(math.trunc(num1//num2))
                print(stack)
            
        return stack[-1]