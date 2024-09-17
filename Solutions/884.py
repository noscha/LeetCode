class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """ Count all words """
        c = Counter(s1.split(' ') + s2.split(' '))
        res = []

        for s in c:
            if c[s] == 1:
                res.append(s)

        return res
