class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        Prefix sum
        """
        vowels = set("aeiou")
        hm, count = {-1:0}, 0
        for i in range(len(words)):
            count += int(words[i][0] in vowels and words[i][-1] in vowels)
            hm[i] = count

        res = []
        for i, j in queries:
            res.append(hm[j] - hm[i - 1])
        return res
