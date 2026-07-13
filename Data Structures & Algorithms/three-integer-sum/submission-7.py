class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            check 
            - if length of array is <3 return []
            - if length == 3, then return array if sum == 0

            possibilities
            - if 0 in array, find x and -x
            - x and y+z such that y+z = -x

            - store results in a set

        '''
        """
        sort array
        if element > 0, break - all eleemnts are positive - cnnot add to 0
        if current element = prev element, skip (continue)
        left pointer = i +1
        right pointer = length -1

        while left pointer < right pointer
        calculte three sum

        if sum = 0 ... append to output list
         - increment left pointer
         - decrement right pointer
         - check for left pointer duplicate and incremenet accordingly
        """
        if len(nums) <3:
            return []
        elif len(nums) == 3:
            return nums if sum(nums) == 0 else []
        
        nums.sort()
        res = []
        l, r = 0, len(nums)-1

        for i, n in enumerate(nums):
            if n>0:
                return res
            if i>0 and n==nums[i-1]:
                continue
    
            l = i+1
            r = len(nums)-1
            while l<r:
                sum3 = n+ nums[l] + nums[r]
                if sum3 == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r-=1
                    l+=1
                elif sum3 <0:
                    l+=1
                else:
                    r-=1
        return res



        
        


                    







        # length = len(nums)

        # output = set()
        # nums.sort()
        # for i in range(length):
        #     for j in range(i+1, length):
        #         for k in range(j+1, length):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 output.add(tuple([nums[i], nums[j], nums[k]]))

        # return [list(x) for x in output]
        