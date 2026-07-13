class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        start, end
        start = 0
        end = 0
        iterate until end >= start
         - sum =  sum + (start - current)
        '''
        if not height:
            return 0
        
        res = 0
        l = 0
        r = len(height)-1
        maxL, maxR = height[l], height[r]

        while l<r:
            if maxL<maxR:
                l+=1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res







        


            
            


        