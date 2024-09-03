class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """ simulate """
        s = list("".join(map(lambda c: str(ord(c) - 96), list(s))))
        s = sum([int(x) for x in s])
        k -= 1
        while k > 0 and s > 9:
            s = sum([int(x) for x in str(s)])
            k -= 1
        return s
