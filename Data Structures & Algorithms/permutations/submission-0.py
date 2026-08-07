class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            if i>=len(nums) and len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for p in nums:
                if p not in cur:
                    cur.append(p)
                    dfs(i+1, cur)
                    cur.pop()
                

        dfs(0, [])
        return res