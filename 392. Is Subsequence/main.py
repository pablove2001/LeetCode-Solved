#7:40min
def main(s, t):
    x = 0
    if s == t:
        return True
    if s == '':
        return True
    if t == '':
        return False
    for letter in t:
        if s[x] == letter:
            x+=1
        if x == len(s):
            return True
    return False


s1 = 'abc'
t1 = 'ahgdc'

print(main(s1, t1))