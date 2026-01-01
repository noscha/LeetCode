class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Sumation with carry
        """

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
           
            if carry == 0:
                return digits

            if digits[i] != 9:
                digits[i] += 1
                carry = 0

            else:
                digits[i] = 0

        if carry:

            return [1] + digits

        return digits
