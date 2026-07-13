class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # SOLUTION WITH HASHMAP
        # hashmap = {}
        # for i, n in enumerate(numbers):
        #     diff = target-n
        #     if diff in hashmap:
        #         return [hashmap[diff]+1, i+1]
        #     hashmap[n] = i

        #SOLUTION WITH POINTERS
        l, r = 0, len(numbers)-1
        while l<r:
            sumn = numbers[l] + numbers[r]
            if sumn == target:
                return [l+1, r+1]
            elif sumn < target:
                l+=1
            else:
                r-=1
            