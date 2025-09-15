class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Split list
        Iterate over each char to check if in 'brokenLetters'
        """

        res = 0
        l = text.split(" ")

        for s in l:
            for c in s:
                if c in brokenLetters:

                    res += 1
                    break
        
        return len(l) - res
