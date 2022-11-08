def main(s):
    l = list(s)
    l.sort()
    cnt = 0

    i = 0
    while len(l)-1 > i:
        if l[i] == l[i+1]:
            l.pop(i)
            l.pop(i)
            cnt += 2
        else:
            i += 1
    print(l)
    if l == []:
        return cnt
    return cnt + 1

s = 'abccccdd'
print(main(s))