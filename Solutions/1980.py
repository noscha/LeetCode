class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Store strings in hash set, and count until one number not in hash set
        """

        n = len(nums[0])
        s = set(nums)

        for i in range(2 ** n):
            key = "{0:b}".format(i).zfill(n)

            if key not in s:
                return key

            s.remove(key)

        return "-1"
      
