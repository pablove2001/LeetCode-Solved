class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        c1 = ''
        c2 = ''
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
                if cnt == 1:
                    c1 = s1[i]
                    c2 = s2[i]
                elif cnt == 2:
                    if c1 != s2[i] or c2 != s1[i]:
                        return False
                else:
                    return False
        if cnt == 0 or cnt == 2:
            return True
        return False
