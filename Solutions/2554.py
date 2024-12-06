class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        """
        Greedily pick the smallest possible numbers
        """
        banned = {i for i in banned if i <= n}
        s, res = 0, 0
        for i in range(1, n + 1):
            if i not in banned and s + i <= maxSum:
                s += i
                res += 1
        return res
