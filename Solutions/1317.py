class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        Brute Force
        """

        for i in range(n // 2 + 1):
            if '0' not in  str(i) + str(n - i) and i + (n - i) == n:
                return [i, n - i]
        return []
