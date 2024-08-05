class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """ Count all string, and check if distinct """
        c = Counter(arr)
        for s in arr:
            k -= (c[s] == 1)
            if not k: return s
        return ""
