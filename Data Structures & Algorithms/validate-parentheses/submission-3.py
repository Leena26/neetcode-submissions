class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        
        hashmap = {'{':'}', '[':']', '(':')'}
        stack  = []
        for i in s:
            if i in hashmap.keys():
                stack.append(i)
            else:
                if hashmap[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0



