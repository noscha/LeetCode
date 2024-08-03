class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """ Compare two hash maps """
        return Counter(target) == Counter(arr)
