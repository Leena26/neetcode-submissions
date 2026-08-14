class Solution:
    def canJump(self, nums: List[int]) -> bool:
        map = {}
        def dfs(i):
            if i in map:
                return map[i]
            if i == len(nums) - 1:
                return True
            if nums[i] == 0:
                return False

            end = min(len(nums), i + nums[i] + 1)
            for j in range(i+1, end):
                if dfs(j):
                    map[i]= True
                    return True
            map[i] = False
            return False
    
        return dfs(0)

        
