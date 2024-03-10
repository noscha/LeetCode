class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ''' Use inbuilt intersection method of sets '''
        return set(nums1).intersection(set(nums2))
