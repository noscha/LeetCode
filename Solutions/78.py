class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ DFS, include element or don't """
        res = []

        def inner(i, curr):
            if i == len(nums):
                res.append(curr)
                return
            inner(i + 1, curr)
            inner(i + 1, curr + [nums[i]])

        inner(0, [])
        return res
        
