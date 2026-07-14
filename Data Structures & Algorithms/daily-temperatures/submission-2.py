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

        output = [0 for x in range(len(temperatures))]
        stack = []
        for i, n in enumerate(temperatures):
            while stack and n>stack[-1][0]:
                tmp = stack.pop()
                output[tmp[1]] = i-tmp[1]
            stack.append([n, i])
        
        return output



        
        
        