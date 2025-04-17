class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        """
        Brute Force, two loops
        """

        res = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):

                res += int(nums[i] == nums[j] and (i * j) % k == 0)

        return res
