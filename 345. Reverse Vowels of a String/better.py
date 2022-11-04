

def main(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    p1 = 0
    p2 = len(s)-1
    arr = list(s)

    ok1 = True
    ok2 = True

    while p1 < p2:
        ok1 = True
        ok2 = True
        if not (arr[p1] in vowels):
            print(f'p1 = {p1}')
            p1 += 1
            ok1 = False
        if not (arr[p2] in vowels):
            print(f'p2 = {p2}')
            p2 -= 1
            ok2 = False
        if ok1 and ok2:
            presta = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = presta
            p1 += 1
            p2 -= 1
    return "".join(arr)






s1 = 'hello wOrlda'
print(main(s1))