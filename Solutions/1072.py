class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """ Find pairs that are the same or bit flipped """
        hm = defaultdict(int)
        for row in matrix:
            row = row if row[0] == 0 else map(lambda x: abs(1 - x), row)
            row = "".join([str(i) for i in row])
            hm[row] += 1
        return max(hm.values())
