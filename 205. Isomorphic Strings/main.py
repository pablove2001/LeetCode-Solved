#13 min
def main(s,t):
    arrS = list(s)
    arrT = list(t)
    arr1 = []
    arr2 = []
    for i in range(len(s)):
        if arrS[i] in arr1:
            index = arr1.index(arrS[i])
            if arr2[index] != arrT[i]:
                return False
        else:
            if arrT[i] in arr2:
                return False
            arr1.append(arrS[i])
            arr2.append(arrT[i])
    return True




s1 = 'paper'
t1 = 'title'

print(main(s1, t1))