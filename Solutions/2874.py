class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Greedy
        """
        largest, max_diff, res = 0, 0, 0
        for i in nums:
            res = max(res, max_diff * i)
            largest = max(largest, i)
            max_diff = max(max_diff, largest - i)
        return res
