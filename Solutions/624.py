class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        """ First check for max diff, then update min/max  """

        arrays = iter(arrays)
        i = next(arrays)
        minimum, maximum, res = i[0], i[-1], 0

        for i in arrays:
            res = max(
                abs(i[0] - maximum),
                abs(i[-1] - minimum),
                res
            )

            minimum = min(minimum, i[0])
            maximum = max(maximum, i[-1])
            
        return res
