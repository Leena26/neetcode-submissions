class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for i,n in enumerate(numbers):
            num = target -n
            if num in prevMap:
                if prevMap[num] > i:
                    return [i+1, prevMap[num]+1]
                return [prevMap[num]+1, i+1]
            prevMap[n] = i
        return