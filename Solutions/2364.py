class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        Find all i == nums[i], then calculate good pairs with little gauss
        """
        
        index_is_value = 0
        litle_gauss = lambda n : (n*(n+1)) / 2
        total_pairs = litle_gauss(len(nums) - 1)
        good_pairs = 0
        count = defaultdict(int)

        for i in range(len(nums)):
            count[nums[i] - i] += 1
            
        for i in count.values():
            if i > 1:
               good_pairs += litle_gauss(i - 1)

        return int(total_pairs - good_pairs)
