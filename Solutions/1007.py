class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Count occurrences of first domino values and take least seen amount as rotations
        """

        n = len(tops)
        top_value, top_seen_top_value, bottom_seen_top_value = tops[0], 0, 0
        bottom_value, top_seen_bottom_value, bottom_seen_bottom_value = bottoms[0], 0, 0
        double_tops, double_bottoms = 0, 0

        for i in range(n):

            if tops[i] == top_value and bottoms[i] != top_value:
                top_seen_top_value += 1

            if tops[i] == bottom_value and bottoms[i] != bottom_value:
                top_seen_bottom_value += 1

            if bottoms[i] == top_value and tops[i] != top_value:
                bottom_seen_top_value += 1

            if bottoms[i] == bottom_value and tops[i] != bottom_value:
                bottom_seen_bottom_value += 1

            if tops[i] == bottoms[i] == top_value:
                double_tops += 1

            if tops[i] == bottoms[i] == bottom_value:
                double_bottoms += 1

        res_0, res_1 = float('inf'), float('inf')

        if top_seen_top_value + bottom_seen_top_value + double_tops == n:
            res_0 = min(top_seen_top_value, bottom_seen_top_value)

        if top_seen_bottom_value + bottom_seen_bottom_value + double_bottoms == n:
            res_1 = min(top_seen_bottom_value, bottom_seen_bottom_value)

        res = min(res_0, res_1)

        return res if res != float("inf") else -1
