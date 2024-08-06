class Solution:
    def minimumPushes(self, word: str) -> int:
        """ Count chars and for each eight chars use one more tap """
        c = Counter(word)
        res, i = 0, 0
        for k, v in c.most_common():
            res += (i // 8 + 1) * v
            i += 1
        return res
