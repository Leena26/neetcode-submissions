class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1:
            return len(s)
        hashSet = set()
        l, r = 0, 0
        res = 0

        while r<len(s):
            if s[r] not in hashSet:
                hashSet.add(s[r])
                r+=1
            else:
                while s[r] in hashSet:
                    hashSet.remove(s[l])
                    l+=1
            res = max(res, r-l)
        return res
        