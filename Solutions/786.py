class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        """ Brute Force solution """
        hm = {}
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                hm[arr[i] / arr[j]] = [arr[i], arr[j]]
        keys = list(hm.keys())
        keys.sort()
        return hm[keys[k-1]]
