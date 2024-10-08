class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """ Bitmask encodes 0: even, 1: odd count of vowels"""
        
        bit_shift = {'a':4, 'e':3, 'i':2, 'o':1, 'u':0}
        hm = {0: -1}
        prev = 0
        res = 0

        for i in range(len(s)):

            mask = prev ^ 1 << bit_shift[s[i]] if s[i] in bit_shift else prev

            if mask in hm:
                res = max(res, i - hm[mask])
            else:
                hm[mask] = i

            prev = mask
            
        return res
