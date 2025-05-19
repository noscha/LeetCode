class Solution:
    def triangleType(self, nums: List[int]) -> str:
        """
        Check if triangle, then check for amount of different sides
        """
        
        if not (nums[0] + nums[1] > nums[2] and
            nums[0] + nums[2] > nums[1] and
            nums[1] + nums[2] > nums[0]):
            
            return "none"

        l = len(set(nums))

        if l == 1:
            return "equilateral"
        elif l == 2:
            return "isosceles"
        else:
            return "scalene"

        return -1
