class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        Keep track of current sum
        """

        s, res = nums[0], nums[0]

        for i in range(1, len(nums)):

            if nums[i] <= nums[i-1]:
                res = max(s, res)
                s = 0

            s += nums[i]

        return max(s, res)
        
