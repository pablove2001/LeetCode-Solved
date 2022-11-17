class Solution:
    def decodeString(self, s: str) -> str:
        res = num = ''
        p1 = cnt = i = 0
        while i < len(s):
            if s[i].isnumeric() and p1 == 0:
                num += s[i]
            elif s[i] == '[':
                if cnt == 0:
                   p1 = i 
                cnt += 1
            elif s[i] == ']':
                cnt -= 1
                if cnt == 0:
                    res += int(num)*self.decodeString(s[p1+1:i])
                    p1 = 0
                    num = ''
            elif cnt == 0:
                res += s[i]
            i += 1
        return res