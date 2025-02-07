class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        """
        Store how many balls belong to each color
        """

        balls = defaultdict(set)
        colors = defaultdict(int)
        res = []
        for i, j in queries:

            if colors[i]:  # for first entry
                balls[colors[i]].remove(i)

                # remove empty keys
                if not balls[colors[i]]:
                    balls.pop(colors[i])

            colors[i] = j
            balls[j].add(i)
            res.append(len(balls))
            
        return res
