class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ''' List comprehension with sorted" '''
        return sorted(i ** 2 for i in nums)
