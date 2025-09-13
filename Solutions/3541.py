class Solution:
    def maxFreqSum(self, s: str) -> int:
        """
        Count all entries and find both maximums
        """

        c = Counter(s)
        max_vovel, max_consonant = 0, 0

        for i in c:

            if i in {'a', 'e', 'i', 'o', 'u'}:
                max_vovel = max(max_vovel, c[i])
            else:
                max_consonant = max(max_consonant, c[i])

        return max_vovel + max_consonant
