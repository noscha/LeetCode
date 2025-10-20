class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        Count occurrence
        """
        
        res = 0

        for o in operations:

            res += 1 if '+' in o else -1

        return res
