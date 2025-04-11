class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        Check for each element if symmetric.
        """

        res = 0

        for i in range(low, high + 1):
            l = [int(x) for x in str(i)]
            if len(l) % 2 == 0:
                res += int(sum(l[:len(l)//2]) == sum(l[len(l)//2:]))
        return res
