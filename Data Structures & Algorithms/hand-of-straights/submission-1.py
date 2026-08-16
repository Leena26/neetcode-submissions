class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        
        freq = Counter(hand)
        hand.sort()
        
        for i in hand:
            if freq[i]:
                for j in range(i, i+groupSize):
                    if not freq[j]:
                        return False
                    freq[j] -=1
        return True
