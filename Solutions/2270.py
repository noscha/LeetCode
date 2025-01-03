class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        Keep track of left and right sum
        """
        right_sum = sum(nums) - nums[0]
        left_sum = nums[0]
        res = 0
        for i in range(1, len(nums)):
            if left_sum >= right_sum:
                res += 1
            right_sum -= nums[i]
            left_sum += nums[i]
        return res
