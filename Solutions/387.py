class Solution:
    def firstUniqChar(self, s: str) -> int:
        """ Store the occurrence of chars in hash map and then look for the occurrence of one """
        hm = {}
        for i in s:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
        for i in hm:
            if hm[i] == 1:
                return s.index(i)
            
        return -1
