class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        """ Iterate over matrix and check if element is lucky number """
        res = []

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == min(matrix[y]) and matrix[y][x] == max([i[x] for i in matrix]):
                    res.append(matrix[y][x] )

        return res
