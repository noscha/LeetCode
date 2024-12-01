class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        For each element, check if 2x or 0.5x were already seen
        """
        hs = set()
        for i in arr:
            if (2 * i) in hs or (i / 2 in hs):
                return True
            hs.add(i)
        return False
