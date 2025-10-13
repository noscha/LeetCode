class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        Check if hash map of current entry equals next.
        """

        c_current = Counter(words[0])
        i = 0

        while i + 1 < len(words):

            c_next = Counter(words[i + 1])

            if c_current == c_next:

                del words[i + 1]

            else:

                i += 1
                c_current = c_next

        return words
