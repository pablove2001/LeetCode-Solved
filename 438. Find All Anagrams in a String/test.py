def main(s, p):
    p = ''.join(sorted(p))
    arr = []
    for i in range(len(s)-len(p)+1):
        if ''.join(sorted(s[i:i+len(p)])) == p:
            arr.append(i)
    return arr


s = "abab"
p = "ab"
print(main(s, p))

# print(isAnagram(p, 'bcs'))




