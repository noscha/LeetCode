class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        Two pointers, one for each string. It is checked whether a character or it's plus one,
        equals a character from str2.
        """
        p1, p2 = 0, 0
        while p1 < len(str1) and p2 < len(str2):
            print(p1, p2)
            if str1[p1] == str2[p2] or chr(((ord(str1[p1]) - 97 + 1) % 26) + 97)  == str2[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        return p2 == len(str2)
