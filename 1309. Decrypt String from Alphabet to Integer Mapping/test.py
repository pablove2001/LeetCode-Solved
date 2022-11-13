def main(s):
    res = ""
    i = len(s)-1
    while i >= 0:
        if s[i] == '#':
            res = chr(int(s[i-2:i])+96) + res
            i-=2
        else:
            res = chr(int(s[i])+96) + res
        i-=1
    return res




s = '10#11#12'
print(main(s))