class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Just do ans[i] = nums[nums[i]]
        """

        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans
