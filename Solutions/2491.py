class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """ Sort and check if first and last elements have same sum """
        skill.sort()
        r, l = 0, len(skill) - 1
        combined = skill[r] + skill[l]
        res = 0
        while r < l:
            if skill[r] + skill[l] != combined:
                return -1
            res += (skill[r] * skill[l])
            r += 1
            l -= 1
        return res
