class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Return False if sum is odd
        DP
        """

        if sum(nums) % 2:
            return False

        total_sum = sum(nums) // 2
        hm = {}

        def dp(curr_sum, index):

            if (curr_sum, index) in hm:
                return hm[(curr_sum, index)]

            if curr_sum == total_sum:
                return True

            if curr_sum > total_sum or index >= len(nums):
                return False

            t0 = dp(curr_sum + nums[index], index + 1)

            if t0:
                return True
                
            t1 = dp(curr_sum , index + 1)

            hm[(curr_sum + nums[index], index + 1)], hm[(curr_sum , index + 1)] = t0, t1

            return max(t0, t1)

        return dp(0, 0)
