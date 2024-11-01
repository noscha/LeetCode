class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        Check if character k is unequal to two previous
        """
        if len(s) < 3:
            return s
            
        res = [s[0], s[1]]
        for i, j, k in zip(s, s[1:], s[2:]):
            if not (i == j and j == k):
                res.append(k)
        return "".join(res)
