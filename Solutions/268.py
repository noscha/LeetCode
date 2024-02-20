class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ''' Iterate over the interval [0, len(nums) +1] and return missing element '''
        nums = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
