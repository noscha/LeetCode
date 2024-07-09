class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """ Simulation """
        cur, res = 0, 0
        for a, t in customers:
            if a > cur:
                cur = a
            cur += t
            res += cur - a
        return res/len(customers)
