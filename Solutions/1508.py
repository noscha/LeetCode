class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """ Create array and return sum """

        sub_arrays = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                sub_arrays.append(s)

        sub_arrays.sort()
        return sum(sub_arrays[left - 1:right]) % (10**9 + 7)
