class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            return min(nums)

            def find_min(l, r):
                if l == r or nums[l] < nums[l]<nums[end]:
                    return l
                
                mid = (l + r) // 2
                if nums[mid] >= nums[start]
                    return find_min(mid+1, r)
                return find_min(l, mid)

        '''
        def find_min(start, end):
            if start==end or nums[start]<nums[end]:
                return start
            mid = (start+end)//2
            if nums[mid]>=nums[start]:
                return find_min(mid+1,end)
            return find_min(start,mid)

        return nums[find_min(0,len(nums)-1)]



        