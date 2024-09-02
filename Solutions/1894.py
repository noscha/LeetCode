class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        """ Find smallest invariant than simulate """

        k = k % sum(chalk)
        i = 0
        while k >= chalk[i]:
            k -= chalk[i]
            i += 1
        return i
