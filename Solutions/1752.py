class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Check for only one order break
        """
        
        no_rotation = True

        for i in range(1,len(nums)):
            if nums[i] < nums[i-1] and no_rotation:
                no_rotation = False
                continue
            elif nums[i] < nums[i-1]:
                return False

        if no_rotation:
            return True

        # for rotation to happen, first element needs to be larger than last
        return not no_rotation and nums[0] >= nums[-1]
