class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Sliding window
        """

        counter = defaultdict(int)
        l, res = 0, 0
        for r in range(len(s)):
            counter[s[r]] += 1

            while len(counter) == 3:
                res += len(s) - r
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    counter.pop(s[l])
                l += 1

        return res
