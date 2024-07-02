class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ Iterate over all elements and count """
        c, res = Counter(nums1), []
        for i in nums2:
            if c[i] > 0:
                res.append(i)
                c[i] -= 1
        return res
