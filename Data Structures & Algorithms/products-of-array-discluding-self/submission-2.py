class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = []

        if 0 in nums:
            if Counter(nums)[0] > 1:
                return [0 for x in range(len(nums))]
            for x in nums:
                if x!=0:
                    product *=x
            for x in nums:
                if x == 0:
                    output.append(product)
                else:
                    output.append(0)
        else:
            for x in nums:
                product *= x
            for x in nums:
                output.append(int(product/x))
        
        return output



        