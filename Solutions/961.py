class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        """
        Boyer–Moore majority algorithm + first three distinction
        """

        if nums[0] == nums[1]:
            return nums[0]

        if nums[1] == nums[2]:
            return nums[1] 

        if nums[0] == nums[2]:
            return nums[2] 


        # Boyer–Moore majority algorithm

        candidate, count = nums[0], 1

        for i in nums[1::]:

            if i == candidate:

                # possible, cause all entries are distinct
                return candidate

            else:

                count -=1

                if count == 0:

                    candidate = i
                    count = 1

        return candidate
