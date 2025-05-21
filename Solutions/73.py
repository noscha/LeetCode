class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Store info in first row and column.
        """

        first_row = -1  # (0, 0) does only encode column
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:

                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        first_row = 0

                    matrix[0][j] = 0

        # set zeros

        for i in range(len(matrix) - 1, 0, -1):

            if matrix[i][0] == 0:

                for j in range(len(matrix[0])):

                    matrix[i][j] = 0
                    

        for j in range(len(matrix[0]) - 1, -1, -1):
            
            if matrix[0][j] == 0:

                for i in range(len(matrix)):

                    matrix[i][j] = 0
        

        if first_row == 0:
            matrix[0] = [0 for i in range(len(matrix[0]))]
