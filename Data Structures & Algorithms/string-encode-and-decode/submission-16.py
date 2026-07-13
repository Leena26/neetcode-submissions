class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for x in strs:
            s = s + str(len(x)) + "#" + x
        return s 

    def decode(self, s: str) -> List[str]:
        x = 0
        res = []
        while x < len(s):
            num = ""
            while s[x] != "#":
                num = num + s[x]
                x +=1
            
            res.append(s[x+1:x+int(num)+1])
            x = x+1+int(num)
        return res
            


        
