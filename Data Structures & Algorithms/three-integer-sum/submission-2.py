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

        length = len(nums)

        output = set()
        nums.sort()
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        output.add(tuple([nums[i], nums[j], nums[k]]))

        return [list(x) for x in output]
        