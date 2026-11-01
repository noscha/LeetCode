class Solution:
    def minMoves(self, nums: list[int]) -> int:
        """
        Increasing n-1 numbers is equivalent to reducing a single number by 1.
        """

        res = 0
        m = min(nums)

        for i in nums:
            res += i - m

        return res
