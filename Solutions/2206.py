class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """
        Count and check if amount is multiple of two
        """
        
        c = Counter(nums)
        for i in c.values():
            if i % 2 == 1:
                return False
        return True
