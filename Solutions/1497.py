class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """ Check if each number has modulo par so together they add to k """
        c = defaultdict(int)
        for i, n in enumerate(arr):
            arr[i] = n % k if n % k >= 0 else (n % k) + k
            c[arr[i]] += 1

        for i in c.keys():
            if i == 0 and not c[i] % 2 == 0:
                return False
            if i > 0 and not c[k - i] == c[i]:
                return False
        return True
