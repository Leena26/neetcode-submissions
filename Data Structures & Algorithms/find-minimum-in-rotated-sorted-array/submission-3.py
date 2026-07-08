class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            return min(nums)

            low = 0
            high = length(nums) -1 (highest index)

            while loop low < = high
                mid = low + high // 2

                if nums[high] < nums[low]:
                    low = mid
                else:
                    high = mid

            return nums[mid]

            mid = 2

        '''
        def find_min(start, end):
            if start==end or nums[start]<nums[end]:
                return start
            mid = (start+end)//2
            if nums[mid]>=nums[start]:
                return find_min(mid+1,end)
            return find_min(start,mid)
            
        return nums[find_min(0,len(nums)-1)]



        