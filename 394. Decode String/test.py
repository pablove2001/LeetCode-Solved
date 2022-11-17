def main(s):
    p1 = 0
    cnt = 0
    res = ''
    num = ''

    i = 0
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
                print(f'{num}*{s[p1+1:i]}')
                res += int(num)*main(s[p1+1:i])
                p1 = 0
                num = ''
        elif cnt == 0:
            res += s[i]
        i += 1
    return res



    

s = "3[a]2[bc3[a]]"
print(main(s))