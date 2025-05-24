class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """
        Loop over everything
        """

        res = []

        for i in range(len(words)):

            if x in words[i]:
                res.append(i)

        return res
