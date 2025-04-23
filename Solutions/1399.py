class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        Store indice sum in hashmap and count largest entries
        """

        hm = defaultdict(int)

        for i in range(1, n + 1):
            
            hm[sum([int(j) for j in str(i)])] += 1

        return list(hm.values()).count(max(hm.values()))
