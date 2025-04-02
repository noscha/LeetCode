class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Brute Force, with three nested loops
        """

        res = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    res = max(res, (nums[i] - nums[j]) * nums[k])

        return res
