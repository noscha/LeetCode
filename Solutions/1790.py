class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Collect different indices, and check (if two) if swaps are applied on same letters
        """
        diff_indices = []

        for i in range(len(s1)):

            if len(diff_indices) > 2:
                return False

            if s1[i] != s2[i]:
                diff_indices.append(i)

        if len(diff_indices) == 2:
            i, j = diff_indices
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        return not diff_indices
