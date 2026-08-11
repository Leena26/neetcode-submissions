class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
                return
            
            for x in range(i, len(s)):
                if self.palindrome(s[i:x+1]):
                    part.append(s[i:x+1])
                    dfs(x+1)
                    part.pop()
        
        dfs(0)
        return res




    def palindrome(self, s):
        return s == s[::-1]   