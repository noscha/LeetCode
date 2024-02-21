class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ''' Find matching bit pattern from the right site and full up with zeros '''
        res = ""
        left = bin(left)[2:]
        right = bin(right)[2:]

        # Base case: if numbers are the same
        if left == right:
            return int(left, 2)
        # Base case: if numbers are of unequal length
        if len(left) != len(right):
            return 0

        
        for i in range(len(left)):
            if left[i] == right[i]:
                res += left[i]
            else:
                res += '0' * (len(left) - i)
                return int(res, 2)
        return int(res, 2)
