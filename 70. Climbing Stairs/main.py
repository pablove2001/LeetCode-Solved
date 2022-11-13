def main(n):
    if n <= 3:
        return n
    n1, n2 = 2, 3
    for i in range(n-3):
        n1, n2 = n2, n2+n1
    return n2

n = 1
for i in range(10):
    print(main(i))
#print(main(n))