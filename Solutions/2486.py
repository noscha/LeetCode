class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """ Two pointers """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            i, j = i + 1, j + int(s[i] == t[j])
        return len(t) - j
