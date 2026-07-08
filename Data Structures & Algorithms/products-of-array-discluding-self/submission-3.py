class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        - one 0: output arr have 0s except when num 0
        - more than 1 0: output arr = all 0s

        - calculte product
        - output[i] = product/nums[i]
        """

        output = []
        product = 1
        if Counter(nums)[0] > 1:
            return [0 for x in range(len(nums))]
        
        if 0 in nums:
            for x in nums:
                if x != 0:
                    product *= x
            
            for x in nums:
                if x==0:
                    output.append(product)
                else:
                    output.append(0)
            
        else:
            for x in nums:
                product *= x
            
            output = [int(product/x) for x in nums]

        return output
        





        