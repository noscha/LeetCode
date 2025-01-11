class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        Single chars can't exceed k and there need to be at least k chars
        """
        c = Counter(s)
        single_chars = 0
        for value in c.values():
            if value % 2 == 1:
                single_chars += 1
        return True if single_chars <= k and len(s) >= k else False
