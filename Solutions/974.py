class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """ Count prefixes with same modulo """
        hm = defaultdict(int)
        hm[0] = 1
        res, s = 0, 0
        for n in nums:
            s += n
            key = s % k
            if key in hm:
                res += hm[key]
            hm[key] += 1
        return res
