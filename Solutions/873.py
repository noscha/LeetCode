class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Treat each possible two numbers as first two fibonacci numbers and check if following exists
        """

        res = 0
        hs = set(arr)

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                
                first, second = arr[j], arr[i] + arr[j]
                fib_size = 2

                while second in hs:
                    first, second = second, first + second
                    fib_size += 1

                res = max(res, fib_size)

        return res if res > 2 else 0
      
