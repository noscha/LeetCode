class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """ Calculate xor prefixes than remove left prefix from right one """

        prefix_xor = [arr[0]]
        for i in range(1, len(arr)):
            prefix_xor.append(arr[i] ^ prefix_xor[-1])

        res = []
        for l, r in queries:
            xor = prefix_xor[r]
            prefix = 0 if l == 0 else prefix_xor[l - 1]
            res.append(xor ^ prefix)
        return res
