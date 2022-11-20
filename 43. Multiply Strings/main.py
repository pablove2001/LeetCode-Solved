class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        
        res = [0]*(l1+l2)
        
        for i, n2 in enumerate(reversed(num2)):
            c = 0
            for j, n1 in enumerate(reversed(num1)):
                pr = (ord('0')-ord(n2))*(ord('0')-ord(n1))
                pr += res[j+i]
                c = pr // 10
                res[j+i+1] += c
                res[j+i] = pr % 10
        
        s = ''
        for i in res:
            s = str(i)+s
        
        return str(int(s))