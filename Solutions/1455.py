class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Split sentence and look for matching beginning with string slicing
        """

        sentence = sentence.split(" ")

        for i, word in enumerate(sentence):
            if len(word) >= len(searchWord) and word[0:len(searchWord) ] == searchWord:
                return i + 1
        else:
            return -1
