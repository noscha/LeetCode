class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        """
        Use stack to process and find coprime with greatest common divisor
        """
        
        res = []

        while nums:

            res.append(nums.pop())

            while len(res) > 1 and math.gcd(res[-2], res[-1]) > 1:

                res.append(math.lcm(res.pop(), res.pop()))

        return res[::-1]
