class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """ Sort with custom function """
      
        c = Counter(nums)
        nums.sort(key=lambda x: (c[x], -x))
        return nums
