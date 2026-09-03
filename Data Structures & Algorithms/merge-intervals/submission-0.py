class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for l, r in intervals:
            lastStart = res[-1][0]
            lastEnd = res[-1][1]

            if l <= lastEnd:
                res[-1][1] = max(lastEnd, r)
            else:
                res.append([l, r])
        return res

        