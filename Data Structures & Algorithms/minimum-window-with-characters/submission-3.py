class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s):
            return ""
        
        letter = Counter(t)
        l, r = 0, len(t)-1
        while r < len(s):
            while letter <= Counter(s[l:r+1]):
                if len(res) >= len(s[l:r+1]) or not res:
                    res = s[l:r+1]
                l +=1
            r+=1
        return res
            



    

