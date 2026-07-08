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
        output = []
        nums.sort()

        for i, a in enumerate(nums):
            if a >0:
                break
            
            if i>0 and a == nums[i-1]: # for index > 0, if current element and prev are equal:
                continue
            
            #two pointers
            l = i+1
            r = len(nums)-1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    output.append([a, nums[l], nums[r]])
                    l +=1
                    r -=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif threeSum > 0:
                    r -=1
                else:
                    l +=1

        return output

                    







        # length = len(nums)

        # output = set()
        # nums.sort()
        # for i in range(length):
        #     for j in range(i+1, length):
        #         for k in range(j+1, length):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 output.add(tuple([nums[i], nums[j], nums[k]]))

        # return [list(x) for x in output]
        