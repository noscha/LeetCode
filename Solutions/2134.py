class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """ Maximum sliding window """

        n, amount_ones = len(nums), nums.count(1)
        l, one_count, max_one_count = 0, 0, 0

        for r in range(len(nums) * 2):

            if r - l >= amount_ones:
                l += 1
                one_count -= nums[l % n - 1]

            if nums[r % n]:
                one_count += 1
                max_one_count = one_count if one_count > max_one_count else max_one_count

        return amount_ones - max_one_count
