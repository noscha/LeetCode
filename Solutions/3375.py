class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Count numbers larger or equal to k
        """

        nums.append(k)
        c = Counter(nums)
        return len(c.keys()) - 1 if min(c.keys()) >= k else -1
