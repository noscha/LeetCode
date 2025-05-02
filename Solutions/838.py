  class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Keep track of right and left timestamps
        """

        left, right = [float for i in range(len(dominoes))], [0 for i in range(len(dominoes))]
        leftCount , rightCount = float('inf'), float('inf')

        for i in range(len(dominoes)):

            if dominoes[i] == "R":
                 rightCount = 1

            if dominoes[i] == "L":
                 rightCount = float('inf')

            if dominoes[len(dominoes) - 1 - i] == "L":
                 leftCount = 1

            if dominoes[len(dominoes) - 1 - i] == "R":
                 leftCount = float('inf')

            right[i] = rightCount
            rightCount += 1

            left[len(dominoes) - 1 - i] = leftCount
            leftCount += 1

        
        # construct result
        res = [0 for i in range(len(dominoes))]

        for i in range(len(dominoes)):

            if left[i] < right[i]:
                res[i] = "L"

            elif left[i] > right[i]:
                res[i] = "R"

            else:
                res[i] = "."

        return "".join(res)
