class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        prev_skill = skill[0] + skill[-1]
        l, r = 0, len(skill)-1
        res = 0
        while l < r:
            if skill[l] + skill[r] != prev_skill:
                return -1
            prev_skill = skill[l] + skill[r]
            res += skill[l] * skill[r]
            l += 1;r -= 1
        return res
