class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """ Math """
        return n - 1 - (time - 1) % (n - 1) if (time - 1) // (n - 1) % 2 else (time - 1) % (n - 1) + 2
