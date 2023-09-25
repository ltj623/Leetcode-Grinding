class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        res = 0
        print(skill)
        tmp = set()
        tmp.add(skill[0] + skill[-1])
        l, r = 0, len(skill)-1
        while l < r:
            if skill[l] + skill[r] not in tmp: 
                return -1
            tmp.add(skill[l] + skill[r])
            res += skill[l] * skill[r]
            l += 1; r -= 1
        return res

        