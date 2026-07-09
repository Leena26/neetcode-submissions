class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for x, y in enumerate(nums):
            diff = target - y
            if diff in hashmap:
                return [hashmap[diff], x]
            hashmap[y] = x
        
        