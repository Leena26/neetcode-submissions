class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        input: array of integers
        output: arrayof integers

        # zeros > 1 -> output of 0s

        prefix: running product up to current
        postfix: end -> start
        """
        n = len(nums)
        res = [1 for x in range(n)]

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        





        