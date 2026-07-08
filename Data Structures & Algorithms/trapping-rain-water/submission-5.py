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
        l, r = 0, len(height)-1
        maxl = height[l]
        maxr = height[r]

        while l < r:
            if maxl < maxr:
                l +=1
                maxl = max(height[l], maxl)
                tmp = maxl - height[l]
                if tmp > 0:
                    res +=tmp
            else:
                r -=1
                maxr = max(height[r], maxr)
                tmp = maxr - height[r]
                if tmp > 0:
                    res += tmp
        return res

        

            





        return res


            
            


        