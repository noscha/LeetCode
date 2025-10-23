class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """
        Simulate
        """

        s, next_s = [int(c) for c in s], []

        while len(s) > 2:

            for i in range(1, len(s)):
                next_s.append((s[i-1] + s[i]) % 10)

            s, next_s = next_s, []

        return s[0] == s[1]
