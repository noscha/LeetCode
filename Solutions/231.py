class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """ Get binary representation of int and check if it contains only one one """
        res = bin(n).count("1")
        return res if res == 1  and n > 0 else 0
