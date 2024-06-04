class Solution:
    def longestPalindrome(self, s: str) -> int:
        """ Two equal chars and if applicable one in the middle is needed """
        hs,res = set(), 0
        for c in s:
            if c in hs:
                hs.remove(c)
                res += 2
            else:
                hs.add(c)
        return res + int(bool(hs))
