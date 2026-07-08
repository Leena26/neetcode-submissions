class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        - one 0: output arr have 0s except when num 0
        - more than 1 0: output arr = all 0s

        - calculte product
        - output[i] = product/nums[i]
        """

        res = [1 for x in nums]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        





        