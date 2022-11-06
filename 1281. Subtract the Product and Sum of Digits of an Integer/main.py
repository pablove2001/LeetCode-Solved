def main(n):
    s = str(n)
    sum = 0
    pro = 1
    for i in s:
        num = int(i)
        sum += num
        pro *= num
    return pro - sum

n = 234
print(main(n))