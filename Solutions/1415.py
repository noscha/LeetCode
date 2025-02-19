class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Create with backtracking strings in lexicographical order
        """

        def backtacking(s: list):
            nonlocal k

            if len(s) == n and k == 1:
                return s

            if len(s) == n:
                k -= 1
                return []

            for i in ["a", "b", "c"]:
                if s and i == s[-1]:
                    continue
                s.append(i)
                res = backtacking(s)
                if res:
                    return res
                s.pop()

            return ""

        return "".join(backtacking([]))
