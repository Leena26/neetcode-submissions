class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        option = ['(', ')']
        def dfs(openC, closeC):
            if openC == n and closeC == n:
                res.append("".join(cur))
                return
            
            if openC < n:
                cur.append("(")
                dfs(openC+1, closeC)
                cur.pop()
            if closeC < openC:
                cur.append(")")
                dfs(openC, closeC+1)
                cur.pop()
        dfs(0, 0)
        return res

