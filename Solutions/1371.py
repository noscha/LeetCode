class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """ Bitmask encodes 0: even, 1: odd count of vowels"""
        
        bit_shift = {'a':4, 'e':3, 'i':2, 'o':1, 'u':0}
        prev = 1 << bit_shift[s[0]] if s[0] in bit_shift else 0
        hm = {0: -1}
        if prev != 0:
            hm[prev] = 0
        res = 0

        for i in range(1, len(s)):

            mask = prev ^ 1 << bit_shift[s[i]] if s[i] in bit_shift else prev

            if mask in hm:
                res = max(res, i - hm[mask])
            else:
                hm[mask] = i

            prev = mask
            
        return res
