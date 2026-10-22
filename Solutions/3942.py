class Solution:
    def minOperations(self, nums: List[int]) -> int:

        """
        Check if cyclic and where cycle starts.
        Extra rotation needed if cycle start closer to end, so we need less shifts.
        """

        if len(nums) == 1:
            return 0

        cliff_pos = 0  # pos where cycle starts
        increasing, decreasing  = False, False
        
        for i in range(len(nums) - 1):
            
            diff = nums[i] - nums[i + 1]

            if diff == -1:

                increasing = True

            elif diff == 1:

                decreasing = True

            elif abs(diff) == len(nums) - 1:

                cliff_pos = i + 1

            else:

                return -1

        if increasing:

            return min(cliff_pos, len(nums) - cliff_pos + 2)

        if decreasing:

            return min(cliff_pos + 1, len(nums) - cliff_pos + 1)
