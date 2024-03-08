class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ''' Count frequency and store maximum, then count occurrence of maximum equals frequency '''
        hm = {}
        maximum = 1

        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
                maximum = hm[i] if hm[i] > maximum else maximum
        res = 0        
        for i in hm:
            if hm[i] == maximum:
                res += hm[i]
        return res
