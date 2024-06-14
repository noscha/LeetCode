class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """ Sort and assure left neighbor is smaller """
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                res += (nums[i - 1] - nums[i] + 1)
                nums[i] += (nums[i - 1] - nums[i] + 1)
        return res
