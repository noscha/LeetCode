class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ''' Solved with recursion and backtracking '''
        visited = set()

        def helper(x, y, i):

            if (x < 0 or x >= len(board) or
                y < 0 or y >= len(board[0]) or
                word[i] != board[x][y] or
                (x, y) in visited):
                return False

            if i == len(word) - 1:
                return True

            visited.add((x, y))
            res = (helper(x + 1, y, i + 1) or
                    helper(x - 1, y, i + 1) or
                    helper(x, y + 1, i + 1) or
                    helper(x, y - 1, i + 1))
            visited.remove((x, y))
            return res
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if helper(x, y, 0):
                    return True
        return False
