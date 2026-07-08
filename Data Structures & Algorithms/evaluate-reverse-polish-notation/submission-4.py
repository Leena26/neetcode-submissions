class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            try:
                int(i)
                stack.append(int(i))
            except:
                if i == "+":
                    tmp = stack.pop() + stack.pop()
                elif i == "-":
                    tmp = stack.pop()
                    tmp = stack.pop() - tmp
                elif i == "*":
                    tmp = stack.pop() * stack.pop()
                else:
                    tmp = stack.pop()
                    tmp = math.trunc(stack.pop() / tmp)
                
                stack.append(int(tmp))
            print(stack)
        return stack.pop()
            

