class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        lp = list(p)
        ls = s.split()

        if len(lp) != len(ls):
            return False

        d = {}

        for i in range(len(lp)):
            if lp[i] in d.keys():
                if d[lp[i]] != ls[i]:
                    return False

            elif ls[i] in d.values():
                return False

            else:
                d[lp[i]] = ls[i]

        return True
