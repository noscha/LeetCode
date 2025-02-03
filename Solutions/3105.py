class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        Track decrease and increase counter
        """
        dec, inc, res = 1, 1, 1
        
        for i in range(1, len(nums)):

            if nums[i] > nums[i-1]:
                inc += 1
                res = max(res, dec)
                dec = 1

            elif nums[i] < nums[i-1]:
                dec += 1
                res = max(res, inc)
                inc = 1

            else:
                res = max(res, inc, dec)
                inc = 1
                dec = 1

        return max(res, dec, inc)
