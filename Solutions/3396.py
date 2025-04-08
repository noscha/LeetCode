class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Find last index where duplicate occurs with hashset.
        """

        hs = set()
        nums = nums[::-1]
        for i in range(len(nums)):
            if nums[i] in hs:
                return math.ceil((len(nums) - i) / 3 )
            hs.add(nums[i])
        return 0
