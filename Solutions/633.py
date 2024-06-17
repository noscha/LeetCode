class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """ Two pointers """
        a, b = 0, int(sqrt(c) + 0.5)
        while a <= b:
            candidate_c = a * a + b * b
            if candidate_c > c:
                b -= 1
            elif candidate_c < c:
                a += 1
            else:
                return True
        return False
