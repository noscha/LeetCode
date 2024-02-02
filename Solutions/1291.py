class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """ Collect all solutions of valid lenght with a sliding window"""
        res = []
        s = "123456789"

        for i in range(len(str(low)), len(str(high)) + 1):
            for j in range(10 - i):
                if low <= int(s[j:j + i]) <= high:
                    res.append(int(s[j:j + i]))
        return res
