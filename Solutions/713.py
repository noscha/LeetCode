class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ''' Solve with sliding window '''
        p0, p1 = 0, 0
        s = 1
        res = 0

        while p1 < len(nums):
            s = s * nums[p1]
            while s >= k and p1 >= p0:
                s = s // nums[p0]
                p0 += 1
            res += p1 - p0 + 1
            p1 += 1
        return res
