class Solution:
    def calculate(self, s: str) -> int:
        s = list(s.replace(' ', ''))
        op = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                op.append(i)
            elif s[i] == ')':
                stringTo = s[op[-1]+1:i]
                s = s[0:op[-1]] + arrToSum(stringTo) + s[i+1:len(s)]
                i = op.pop()-1
            i += 1
        return int("".join(arrToSum(s)))



def arrToSum(s):
    sum = 0
    num = ''
    neg = False
    lastN = False
    for i in s:
        if i == '-' or i == '+':
            if lastN:
                if neg:
                    sum -= int(num)
                else:
                    sum += int(num)
                neg = False
                lastN = False
                num = ''
            if i == '-':
                neg = not neg
        else:
            num += i
            lastN = True    
    if neg:
        return list(str(sum - int(num)))
    return list(str(sum + int(num)))