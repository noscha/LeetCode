class Solution:
    def frequencySort(self, s: str) -> str:
        """ First count occurrences of each char, then sort them and put them together in a string """
        hm = {}
        res = ""
        
        for c in s:
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1

        hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))

        for i in hm:
            res += hm[i] * i
        return res
