class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ''' Count all chars in s, then arrange them by order '''

        hm = {}
        for i in s:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1

        res = ""
        for i in order:
            if i in s:
                res += (i * hm[i])
                hm[i] = 0

        for i in hm:
            res += (i * hm[i])

        return res
        
