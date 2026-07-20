class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        - map position and speed
        - sort by position
        - to check if two cars collide, we compare time taken to reach target
            - if the further car takes a shorter time, they collide
            - 
        """

        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]

        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)

        
