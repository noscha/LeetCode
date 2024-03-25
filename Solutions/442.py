class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ''' Use seen numbers as index and mark them as negative '''
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] = -(nums[abs(nums[i]) - 1])
        return res
