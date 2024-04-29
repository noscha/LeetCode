class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """ XOR nums and count mismatching bits """
        res = 0
        for i in nums:
            res ^= i
        return (res ^ k).bit_count()
