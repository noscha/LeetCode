class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ''' Create intersection and return min element '''
        hs1 = set(nums1)
        hs2 = set(nums2)
        hsInter = hs1.intersection(hs2)
        return min(hsInter, default=-1)
