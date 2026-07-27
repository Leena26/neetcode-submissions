class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == nums[mid+1]:
                return nums[mid]
            elif nums[mid] < mid+1:
                r = mid-1
            else:
                l = mid+1

        