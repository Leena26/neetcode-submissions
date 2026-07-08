class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i,n in enumerate(nums):
            num = target -n
            if num in prevMap:
                return[prevMap[num], i]
            prevMap[n] = i
        return
        