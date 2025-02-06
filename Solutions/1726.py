class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        Count all products, then for each pair there are "|pairs| nCr 2" combinations
        """

        hm = defaultdict(set)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a, b = nums[i], nums[j]
                hm[a * b].add(a)
                hm[a * b].add(b)
        
        res = 0
        for i in hm.values():
            if len(i) >= 4:
                res += 8 * comb((len(i) // 2), 2)
        return res
      
