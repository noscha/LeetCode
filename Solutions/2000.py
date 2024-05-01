class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """ Look up index with built-in function """
        word = list(word)
        try:
            i = word.index(ch)
        except:
            return "".join(word)
        return "".join(word[i::-1]+word[i + 1::])
