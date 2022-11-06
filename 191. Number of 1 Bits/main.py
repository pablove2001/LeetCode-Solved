
def main(n):
    cnt = 0        
    while(n != 0):
        n = n & (n - 1)
        cnt += 1
        print(n)
    return cnt

n = 14

print(main(n))