class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """ Simualte """
        x, y = 0, 0
        res = 0
        obstacles = {tuple(i) for i in obstacles}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        for c in commands:
            if c == -2:
                direction = (direction - 1) % 4

            elif c == -1:
                direction = (direction + 1) % 4

            else:
                for _ in range(c):
                    d_x, d_y = directions[direction]

                    if (x + d_x , y + d_y) in obstacles:
                        break

                    x, y = x + d_x, y + d_y
                    res = max(res, x ** 2 + y ** 2)

        return res
