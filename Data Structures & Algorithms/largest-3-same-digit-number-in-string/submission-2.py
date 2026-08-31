class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            n = str(i) + str(i) + str(i)
            if n in num:
                return n
        return ""