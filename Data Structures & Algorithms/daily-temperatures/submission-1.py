class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        stack = []
        output [] ... default values of 0 .. ize length(temperature)

        loop
            while stack is not empty and current temperature > most rcent temp added to stack:
                popStack
                output[poppedValue_index] = i - poppedValue_index
            stack append [temperature and index]

        return output

        '''
        length = len(temperatures)
        stack = [] # pair of values [temp, index]
        output = [0 for x in range(length)]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                output[stackI] = i - stackI
            stack.append([t, i])
        return output
        