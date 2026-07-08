class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        maxP = 0
        for i in s:
            if i in string:
                index = string.find(i)
                string = string[index+1::] + i
            else:
                string = string + i
            maxP = max(maxP, len(string))
        return maxP
        