class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """ Look for prefix with same modulo """
        hm = {0:-1}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            key = s % k
            if key not in hm:
                hm[key] = i
            elif i - hm[key] > 1:
                return 1 
        return 0
