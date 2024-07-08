class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """ Simulation """
        q = deque([i + 1 for i in range(n)])
        while len(q) > 1:
            for i in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        return q.pop()
