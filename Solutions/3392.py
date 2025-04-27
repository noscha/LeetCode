class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        Iterate over array and check condition
        """

        res = 0

        for l in range(2, len(nums)):

            res += int((nums[l] + nums[l - 2]) == nums[l - 1] / 2)

        return res
