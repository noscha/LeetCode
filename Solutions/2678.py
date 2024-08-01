class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """ Iterate over details and count """
        res = 0
        for s in details:
            res += int(int(s[11:13]) > 60)
        return res 
