arr = [42, [22,113, [2,3,4, [24,34], 42], [[2]]], 41,25 ,53]
res = []

num = ''
for i in str(arr):
    if i == ',':
        res.append(int(num))
        num = ''
    elif i.isnumeric():
        num += i

print(res)