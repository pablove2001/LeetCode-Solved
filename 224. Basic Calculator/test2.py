def main(s):
    s = list(s.replace(' ', ''))
    op = []

    i = 0
    while i < len(s):
        if s[i] == '(':
            op.append(i)
        elif s[i] == ')':
            stringTo = s[op[-1]+1:i]
            print(stringTo)
            s = s[0:op[-1]] + arrToSum(stringTo) + s[i+1:len(s)]
            print(s)
            i = op.pop()-1
        i += 1
    return arrToSum(s)



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

s = '(1-(4+5+2)-3)+(6+8)'
# s = '(1+11-3)+(6+8)'
# s = '9+(6+8)'
# s = '9+14'
# s = '23'

print(main(s))