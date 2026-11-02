class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        """
        Median minimizes the sum of absolute differences.
        """
        
        nums.sort()
        n = len(nums)
        median = nums[n // 2] if n % 2 else (nums[n//2 - 1] + nums[n//2]) / 2
        res = 0
    
        for i in nums:

            res += abs(i - median)

        return round(res)
