class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """ Sort each index by entry """
        l = []
        for i, e in enumerate(score):
            l.append((e, i))
        l = sorted(l)

        res = [0] * len(score)
        for i in range(len(l)):
            s = len(score) - i
            if s == 1:
                res[l[i][1]] = "Gold Medal"
            elif s == 2:
                res[l[i][1]] = "Silver Medal"
            elif s == 3:
                res[l[i][1]] = "Bronze Medal"
            else:
                res[l[i][1]] = str(s)
        return res
        
