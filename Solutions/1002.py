class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """ Count chars of each string and take minimum """
        res, all_d = [], []
        chars = set(words[0])

        for c in chars:
            m = float("inf")
            for d in [Counter(w) for w in words]:
                m = min(m, d[c])
            for i in range(m):
                res.append(c)
        return res
