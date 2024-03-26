class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ''' Change negatives or zeros with n+1, then use entries as indices and make them negative.
            At the end, find the indice without a negative entry '''
      
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1

        for i in range(len(nums)):
            if 0 <= abs(nums[i]) - 1 <= len(nums) - 1:
                nums[abs(nums[i]) - 1] = -(abs(nums[abs(nums[i]) - 1]))
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1
        
