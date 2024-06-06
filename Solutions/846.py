class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """ Count all occurrences and then greedily look for groups """
        if len(hand) % groupSize != 0:
            return 0

        hand.sort()
        c = Counter(hand)
        k = list(c.keys())
        while k:
            for i in range(k[0], k[0] + groupSize):
                if i not in k:
                    return False
                if c[i] == 1:
                    k.remove(i)
                else:
                    c[i] -= 1 
        return True
