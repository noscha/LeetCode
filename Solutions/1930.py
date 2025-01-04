class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Keep track of left and right side, also of seen palindromes
        """
        seen = set()
        left_chars = defaultdict(int)
        right_chars = Counter(s)
        for i in range(len(s) - 1):
            right_chars[s[i]] -= 1
            for c in left_chars:
                if right_chars[c] > 0:
                    seen.add((s[i], c))
            left_chars[s[i]] += 1
        return len(seen)
