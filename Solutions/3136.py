class Solution:
    def isValid(self, word: str) -> bool:
        """
        Check if string is valid as described
        """
        
        if len(word) < 3:
            return False

        vowel, consonant = False, False
        for c in word:
            if c.isalpha():
                if c.lower() in ["a","e","i","o","u"]:
                    vowel = True
                else:
                    consonant = True

            elif c.isdigit():
                continue

            else:
                return False

        return vowel and consonant
