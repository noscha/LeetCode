class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Store last occurrence of each char in hm.
        Iterate over s and find maximal ending point.
        """

        res = []
        hm = {chr(k) : -1 for k in range(97, 123)}
        
        for i in range(len(s) - 1, -1, -1):
            if hm[s[i]] == -1:
                hm[s[i]] = i

        size, end = 1, 0
        for i in range(len(s)):
            end = hm[s[i]] if hm[s[i]] >= end else end
            if i == end:
                res.append(size)
                size = 0
            size += 1

        return res
