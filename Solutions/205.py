class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ''' Each word parring is stored in a bidirectional hash map '''
        hmST, hmTS = {}, {}
        for i in range(len(s)):
            if (s[i]  in hmST and t[i] != hmST[s[i]]) or (t[i] in hmTS and s[i] != hmTS[t[i]]):
                return False
            hmST[s[i]] = t[i]
            hmTS[t[i]] = s[i]
        return True
