class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        """
        Brute Force
        """

        res = []
        c = Counter([str(i) for i in digits])

        for i in range(100, 999, 2):
            number_c = Counter(list(str(i)))

            contain = True

            for k in number_c:
                if number_c[k] > c[k]:
                    contain = False
                    break

            if contain:
                res.append(i)

        return res
