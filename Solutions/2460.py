class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        Simulate process and swap with two pointers
        """

        for i in range(len(nums) - 1):

            if nums[i] != nums[i + 1]:
                continue

            nums[i] *= 2
            nums[i + 1] = 0

        p = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        
        return nums
