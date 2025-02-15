class Solution:
    def punishmentNumber(self, n: int) -> int:
        """
        Find all partition with backtracking
        """

        def partition(target: int, l: list, s: int, i:int):
        
            if i == len(l) and s == target:
                return True

            for j in range(i, len(l)):
                number = int(''.join(map(str, l[i:j+1])))
                if partition(target, l, s + number, j + 1):
                    
                    return True
            return False
        

        res = 0

        for i in range(0, n + 1):
            l = list(map(int, str(i * i)))

            if partition(i, l, 0, 0):
                res += i *i 

        return res
