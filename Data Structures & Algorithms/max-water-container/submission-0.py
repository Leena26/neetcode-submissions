class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i, a in enumerate(heights):
            right = len(heights)-1
            while i < right:
                height = min(heights[i], heights[right])
                volume = height* (right - i )
                print(res)
                res = max(res, volume)
                right -=1
        
        return res