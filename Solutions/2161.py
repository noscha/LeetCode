class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        Iterate over nums and collect elements into right bucket
        """

        right, pivots, left = [], [], []

        for i in nums:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                pivots.append(i)

        return left + pivots + right
