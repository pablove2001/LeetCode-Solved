def main(n):
    p1 = 1
    p2 = n
    if isBadVersion(p1):
        return p1
    while p2-p1 > 1:
        c = (p2-p1)//2+p1
        if not isBadVersion(c):
            p1 = c
        else:
            p2 = c
    return p2





def isBadVersion(num):
    if num >= 2:
        return True
    return False

n = 8
print(main(n))