class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """ Check consistency via subsets """
        allowed = set(allowed)
        res = 0
        for l in words:
            res += int(set(l).issubset(allowed))
        return res
