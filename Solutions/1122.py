class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """ Count arr1 and use order of arr2 """
        res = []
        c = Counter(arr1)
        for a in arr2:
            res.extend([a for i in range(c[a])])
            del c[a]
        for k in sorted(c.keys()):
            res.extend([k for i in range(c[k])])
        return res
