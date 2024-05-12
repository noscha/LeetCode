class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """" For each tile, iterate over 3×3 neighborhood """
        res = [[-1]*(len(grid) - 2) for i in range(len(grid) - 2)]
        for i in range(len(grid) - 2):
            for j in range(len(grid) -2):
                temp = []
                for k in range(3):
                    for l in range(3):
                        temp.append(grid[i + k][j + l])
                res[i][j] = max(temp)
        return res
        
