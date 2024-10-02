class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """ Sort set and add index """
        hm = {k: v for v, k in enumerate(sorted(set(arr)))}
        return [hm[i] + 1 for i in arr]
