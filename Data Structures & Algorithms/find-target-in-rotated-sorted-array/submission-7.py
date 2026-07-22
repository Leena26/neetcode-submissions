class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
            Brute force:
                if target in nums:
                    return nums.index(target)
                return -1

            O(n)

            ---------

            Binary search 
             - l, r pointers
             - mid middle index
           

            while loop l <= r
              - check if target = nums[mid]: return mid

            Left portion
            - target < nums[l] or target is > nums[mid] -> l = mid +1
            - else: r = mid-1

            Right portion
            - target > nums[r] or target < nums[mid]: r = mid -1
            - else: l = mid +1

            return -1

        '''

        l = 0
        r = len(nums) -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]:
                if target<nums[l] or target> nums[mid]:
                    l = mid +1
                else:
                    r = mid-1
            else:
                if target<  nums[mid] or target > nums[r]:
                    r = mid-1
                else:
                    l = mid+1
            
        return -1


            




        