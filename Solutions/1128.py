class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        Count all dominos, for each count draw two elements unordered and without repetition
        """

        res = 0
        hm = defaultdict(int)

        for i in dominoes:

            i.sort()
            hm[tuple(i)] += 1
        
        for i in hm.values():

            res += math.comb(i, 2)

        return res
