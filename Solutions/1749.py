class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        Kadane's algorithm, twice
        """

        res = nums[0]
        max_ending = nums[0]
        min_ending = nums[0]

        for i in range(1, len(nums)):
            max_ending = max(max_ending + nums[i], nums[i])
            min_ending = min(min_ending + nums[i], nums[i])
            res = max([abs(res), abs(max_ending), abs(min_ending)])

        return abs(res)
