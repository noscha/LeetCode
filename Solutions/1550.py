class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """ Iterate over array to check for three consecutive odd numbers """
        for i in range(2, len(arr)):
            if arr[i - 2] % 2 + arr[i - 1] % 2 + arr[i] % 2 == 3:
                print(i)
                return True
        return False
