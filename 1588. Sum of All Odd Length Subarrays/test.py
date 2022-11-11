def main(arr):
    length = len(arr)
    lenS = 1
    while lenS <= length:
        for i in range(0, length-lenS+2):
            print(f'i:{i} f:{i+lenS}')
            for j in range(i, i+lenS):
                print(f'    {j}')


        lenS += 2

arr = [1,2,3,4,5]
print(main(arr))