class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        Sliding window check for overlapping bits
        Bit mask need to stay zero under "and" operation, for no overlapping bits
        "Or" adds to bit mask
        "Xor" subtracts from bit mask
        """

        l, cur, res = 0, 0, 1
        for r in range(len(nums)):
            while cur & nums[r]:
                cur ^= nums[l]
                l += 1

            cur |= nums[r]
            res = max(res, r - l + 1)

        return res
