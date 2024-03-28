class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ''' Solved with sliding window '''
        res = 0
        hm = defaultdict(int)
        left, right = 0, 0
        while right < len(nums):
            hm[nums[right]] += 1
            while hm[nums[right]] > k:
                hm[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
