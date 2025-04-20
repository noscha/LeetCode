class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        Count all amounts; if occurrence of answer larger than amount, means more than one colour
        """

        c = Counter(answers)
        res = 0

        for i in c:
            res += math.ceil(c[i] / (i + 1)) * (i + 1)

        return res
