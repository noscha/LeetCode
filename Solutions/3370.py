class Solution:
    def smallestNumber(self, n: int) -> int:
        """
        Get length of binary representation and return as many set bits
        """

        return int("".join('1' * len("{0:b}".format(n))), 2)
