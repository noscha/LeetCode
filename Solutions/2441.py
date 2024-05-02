class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        """ For each entry look if negative exists, and store largest """
        nums = set(nums)
        res = -1

        for i in nums:
            res = abs(i) if -i in nums and abs(i) > res else res
        return res
