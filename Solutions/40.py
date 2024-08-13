class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """ Backtracking  and skip elements if we discarded them """
        res = []
        candidates.sort()
        def inner(i: int, l: list[int]) -> None:
            if sum(l) == target:
                res.append(l)
                return

            if i == len(candidates) or sum(l) > target:
                return

            l.append(candidates[i])
            inner(i + 1, l.copy())
            l.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            inner(i + 1, l)
            return

        inner(0, [])
        return res
