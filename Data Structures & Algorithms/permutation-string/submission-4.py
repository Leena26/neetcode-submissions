class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        count1 = Counter(s1)
        l, r = 0, len(s1)-1
        while r < len(s2):
            s = s2[l:r+1]
            if Counter(s) == count1:
                return True
            l+=1
            r+=1
        return False

        