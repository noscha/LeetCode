class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        Dynamic Programming
        """
        mem = [-1] * len(questions)

        def dp(index):

            if index >= len(questions):
                return 0

            if mem[index] != -1:
                return mem[index]

            points, brainpower = questions[index]
            include = points + dp(index + brainpower + 1)
            exclude = dp(index + 1)

            mem[index] = max(include, exclude)
            return mem[index]

        return dp(0)
