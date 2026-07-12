class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, n in enumerate(numbers):
            num = target-n
            if num in hashmap:
                return [hashmap[num]+1, i+1]
            hashmap[n] = i