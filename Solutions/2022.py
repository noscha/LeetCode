class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        """ Iterate over original to construct new """

        if len(original) != m * n:
            return []
        k = 0
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = original[k]
                k += 1
        return res
