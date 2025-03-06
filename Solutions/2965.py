class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        Collect all numbers in hash map
        """

        N = len(grid)
        hm = defaultdict(int)

        for i in range(N):
            for j in range(N):
                hm[grid[i][j]] += 1

        
        for i in range(1, N * N + 1):
            if hm[i] == 0:
                missing = i
            elif hm[i] == 2:
                twice = i

        return [twice, missing]
