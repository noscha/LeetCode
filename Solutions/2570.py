class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        Use merge like in merge-sort
        """

        res = []

        while nums1 and nums2:
            if nums1[0][0] > nums2[0][0]:
                res.append(nums2.pop(0))

            elif nums1[0][0] < nums2[0][0]:
                res.append(nums1.pop(0))

            else:
                e1, e2 = nums1.pop(0), nums2.pop(0)
                res.append([e1[0], e1[1] + e2[1]])

        if nums1:
            res += nums1

        if nums2:
            res += nums2

        return res
      
