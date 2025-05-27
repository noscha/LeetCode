class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """
        Triangular numbers
        """

        d = n // m
        return n * (n + 1) // 2 - d * (d + 1) * m
