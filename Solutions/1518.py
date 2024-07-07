class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """ Simulation """
        res = 0
        full, empty = numBottles , 0
        while full:
            res += full
            empty += full
            full = empty // numExchange
            empty = empty % numExchange
        return res
