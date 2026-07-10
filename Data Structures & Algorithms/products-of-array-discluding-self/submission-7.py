class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        input: array of integers
        output: arrayof integers

        # zeros > 1 -> output of 0s

        prefix: running product up to current
        postfix: end -> start
        """
        if Counter(nums)[0] > 1:
            return [0 for x in range(len(nums))]
        
        res = []
        prod = 1
        for x in nums:
            if x != 0:
                prod *= x
        
        if 0 in nums:
            res = [0 for x in range(len(nums))]
            res[nums.index(0)] = prod
        else:
            res = [int(prod/x) for x in nums]

        return res
        





        