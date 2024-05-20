class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """ DFS, include element or don't """

        def inner(i, res):
            return res if i == len(nums) else inner(i + 1, res ^ nums[i]) + inner(i + 1, res)

        return inner(0, 0)
