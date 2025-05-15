class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        Greedy, start with first bit and look for alternating sequence
        """

        bit = groups[0]
        res = [words[0]]
        for i in range(1, len(groups)):

            if groups[i] != bit:
                bit = groups[i]
                res.append(words[i])

        return res
