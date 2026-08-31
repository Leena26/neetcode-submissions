class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        maxOdd = 0
        minOdd = float("inf")

        for c in count:
            if count[c] %2 == 1:
                maxOdd = max(maxOdd, count[c])
            else:
                minOdd = min(minOdd, count[c])
        return maxOdd-minOdd
