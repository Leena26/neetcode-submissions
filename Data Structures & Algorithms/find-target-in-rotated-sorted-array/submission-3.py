class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
            Brute force:
                if target in nums:
                    return nums.index(target)
                return -1

            O(n)

            ---------

            Binary search twice
             - find where deflection is
             - binry search within the selected part to find target
        '''

        l = 0
        r = len(nums) -1
        while l<=r: 
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid +1
                else:
                    r = mid -1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                else:
                    l = mid +1
        return -1

            




        