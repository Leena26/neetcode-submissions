class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stack = [] # pair of values [temp, index]
        output = [0 for x in range(length)]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                output[stackI] = i - stackI
            stack.append([t, i])
        return output
        