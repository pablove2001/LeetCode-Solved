class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:  
        c = ''
        for i in range(len(s)//2):
            c += s[i]
            if len(s)%len(c)!=0:
                continue
            sb = True
            for j in range(i+1,len(s)-i, i+1):
                if c != s[j:j+i+1]:
                    sb = False
                    break
            if sb:
                return True
        return False