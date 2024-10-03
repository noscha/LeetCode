class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """ Calculate prefix sum with modulo """
        total_sum = sum(nums) % p
        if not total_sum:
            return 0

        current_sum = 0
        hm = {0: -1}
        res = len(nums)

        for i, n in enumerate(nums):
            current_sum = (n + current_sum) % p
            temp = (current_sum - total_sum + p) % p
            if temp in hm:
                res = min(i - hm[temp], res)
            hm[current_sum] = i
        return -1 if res == len(nums) else res
