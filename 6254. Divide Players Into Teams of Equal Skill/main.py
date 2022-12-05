class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        le = len(skill)
        promedio = sum(skill)*2/(le)
        if promedio != int(promedio):
            return -1
        promedio = int(promedio)
        print(promedio)
        res = 0
        skill.sort()
        print(skill)
        for i in range(le//2):
            print(skill[i], skill[le-i-1])
            if skill[i] + skill[le-i-1] != promedio:
                return -1
            res += skill[i] * skill[le-i-1]

        return res