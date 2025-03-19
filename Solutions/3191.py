class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Sliding window, flip at first occurrence of a zero
        """

        l, res = 0, 0

        for r in range(2, len(nums)):
            if not nums[l]:
                for i in range(l, r + 1):
                    nums[i] ^= 1
                res += 1
            l += 1

        return -1 if 0 in nums[-2:] else res
