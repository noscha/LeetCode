class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Backtracking, count all combinations
        """

        c = Counter(tiles)

        def backtracking(res=0) -> int:

            for key in c:
                if c[key] <= 0:
                    continue
                c[key] -= 1
                res += 1
                res += backtracking()
                c[key] += 1
                
            return res

        return backtracking()
