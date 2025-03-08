class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        Find window with most black blocks
        """

        # Initialize sliding window
        black = 0
        for i in range(k):
            black += int(blocks[i] == 'B')

        res, j = black, 0
        for i in range(k, len(blocks)):
            black += int(blocks[i] == 'B')
            black -= int(blocks[j] == 'B')
            res = max(res, black)
            j += 1

        return k - res
