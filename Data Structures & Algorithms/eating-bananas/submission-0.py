class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Brute force
        flag = False
        while not flag:
        '''
        piles.sort()
        high = max(piles)
        low = 1
        res = high

        while low <= high:
            curr = (low + high)//2
            hour = 0
            for i in piles:
                hour += math.ceil(i/curr)
            if hour <= h:
                res = min(res, curr)
                high = curr -1
            else:
                low = curr +1
        return res
                



        