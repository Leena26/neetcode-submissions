class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
            boats = 0

            - sort array
            - two pointers: left 0 and right len(people)-1
            - check if left + right <= limit
                increment boats
            3, 3, 4, 5
        '''

        people.sort()
        l = 0
        r = len(people)-1
        boat = 0

        while l < r:
            if people[l] + people[r] <= limit:
                boat +=1
                l +=1
            elif people[r] <= limit:
                boat +=1
            r -=1
        
        if r == l and people[r] <=limit:
            boat+=1
        
        return boat

            
