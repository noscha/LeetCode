class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Sum of differences to maximum.
        """
        
        maximum = max(nums)
        res = 0

        for i in nums:

            res += maximum - i

        return res
