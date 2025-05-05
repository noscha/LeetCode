class Solution:
    def numTilings(self, n: int) -> int:
        """
        Pattern is f(n + 1) = 2 * f(n) + f(n - 2)
        """
        
        mod = 10 ** 9 + 7
        hm = {1:1, 2:2, 3:5}

        def rec(n: int) -> int:

            if n in hm:
                return hm[n]
            else:
                if n - 1 in hm:
                    temp_0 = hm[n - 1]
                else:
                    temp_0 = rec(n - 1)
                    hm[n - 1] = temp_0 % mod

                if n - 3 in hm:
                    temp_1 = hm[n - 3]
                else:
                    temp_1 = rec(n - 3)
                    hm[n - 3] = temp_1 % mod

                return 2 * temp_0 + temp_1

        return rec(n) % mod
