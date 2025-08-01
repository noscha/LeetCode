class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Fill up rows with zero at both ends.
        Take sum of all two neighbouring elements for next row.
        """

        res = [[1]]

        for i in range(numRows - 1):

            temp = [0] + res[-1] + [0]
            res_appendix = []

            for i in range(len(res[-1]) + 1):
                res_appendix.append(temp[i] + temp[i + 1])

            res.append(res_appendix)

        return res
