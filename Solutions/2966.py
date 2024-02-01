class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """ Sort array and divide it into  segment of size three
        while checking if the diffrence between two neigboring elemnts 
        is les or quual to k """
        res = []
        nums.sort()

        for i in range(0, len(nums), 3):
            temp = nums[i:i + 3]
            if temp[2] - temp[0] > k:
                return []
            res.append(temp)
        return res
