class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack = []
        start = ["{", "[", "("]
        end = ["}", "]", ")"]
        for i in s:
            if i in start:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                index = end.index(i)
                if start[index] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack


