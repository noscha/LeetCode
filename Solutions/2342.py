class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        Store for each digit sums, their number in sorted list.
        Compare largest two entries of sorted lists.
        """

        digit_sums = defaultdict(SortedList)
        for i in nums:
            digit_sum = sum(list(map(int, str(i))))
            digit_sums[digit_sum].add(i)

        res = -1
        for sl in digit_sums.values():
            if len(sl) >= 2:
                sum_largest_tuple = sum(sl[-2:])
                res = max(res, sum_largest_tuple)

        return res
