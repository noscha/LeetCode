class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        """
        Collect sliced strings in list and then join them
        """
        res = []
        prev_i = 0
        for i in spaces + [len(s)]:
            res.append(s[prev_i:i])
            prev_i = i
        return " ".join(res)
