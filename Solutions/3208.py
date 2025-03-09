class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        """
        Sliding window
        """

        res, l = 0, 0
        for r in range(1, len(colors) + k - 1):

            if colors[r % len(colors)] == colors[(r - 1) % len(colors)]:
                l = r
            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                res += 1

        return res
