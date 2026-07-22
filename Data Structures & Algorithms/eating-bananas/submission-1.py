class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Brute force
        flag = False
        while not flag:
        '''
        piles.sort()
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i/k)
            if hours <= h:
                res = k
                r = k -1
            else:
                l = k+1
        return res
                



        