def main(arr):
    length = 1
    res = 0
    while length <= len(arr):
        p1 = 0
        p2 = length
        while p2 <= len(arr):
            print(arr[p1:p2])
            res += sum(arr[p1:p2])
            p1 += 1
            p2 += 1
        length += 2
    return res

arr = [1,2,3,4,5,6]
print(main(arr))