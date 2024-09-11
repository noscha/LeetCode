class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """ Count different bits with xor """
        return bin(start ^ goal).count('1')
