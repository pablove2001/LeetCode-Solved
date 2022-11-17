class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)

        i = len(ls)-1
        cnt = 0
        while i >= 0:
            if ls[i] == '#':
                ls.pop(i)
                cnt += 1
            elif cnt >= 1:
                ls.pop(i)
                cnt -= 1
            i -= 1

        i = len(lt)-1
        cnt = 0
        while i >= 0:
            if lt[i] == '#':
                lt.pop(i)
                cnt += 1
            elif cnt >= 1:
                lt.pop(i)
                cnt -= 1
            i -= 1

        if lt == ls:
            return True
        return False