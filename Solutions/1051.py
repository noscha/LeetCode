class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """ Compare list to sorted """
        c = sorted(heights)
        res = 0
        for i in zip(heights, c):
            if i[0] != i[1]:
                res += 1
        return res
