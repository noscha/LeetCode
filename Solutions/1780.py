class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Divide by three until zero and check if rest is two
        """

        TWO, THREE = 2, 3

        while n:
            r = n % THREE
            n //= THREE
            if r == TWO:
                return False

        return True
