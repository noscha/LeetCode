class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """ calculate missing sum and then be greedy """

        sum_n = mean * (len(rolls) + n)  - sum(rolls)
        # validate sum
        if sum_n > n * 6 or sum_n < n:
            return []

        res = []
        for i in range(n, 0, -1):
            roll = min(6, sum_n - i + 1)
            res.append(roll)
            sum_n -= roll

        return res
