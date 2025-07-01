class Solution:
    def possibleStringCount(self, word: str) -> int:
        """
        For each amount of consecutive chars, amount - 1 possible origins
        """

        res = 0
        cur_char = ""
        cur_char_count = 0

        for i in word:

            if i != cur_char:

                if cur_char_count > 1:
                    res += cur_char_count - 1
                cur_char = i
                cur_char_count = 1

            else:
                cur_char_count += 1

        if cur_char_count > 1:
            res += cur_char_count - 1

        return res + 1
