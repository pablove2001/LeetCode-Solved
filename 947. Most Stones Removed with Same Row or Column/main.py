###################### Incorrect/Incomplete ######################
def main(stones):
    removed = 0
    while True:
        counter = countStones(stones)
        while 0 in counter:
            index0 = counter.index(0)
            stones.pop(index0)
            counter.pop(index0)
        if len(stones) > 1:
            removed += 1
            indexmin = indexMinArr(counter)
            stones.pop(indexmin)
            counter.pop(indexmin)
        else:
            break
    return removed

def countStones(stones):
    counter = [0]*len(stones)
    for i in range(len(stones)-1):
        for j in range(i+1, len(stones)):
            if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                counter[i] += 1
                counter[j] += 1
    return counter

def indexMinArr(arr):
    return arr.index(min(arr))


stones = [[5,9],[9,0],[0,0],[7,0],[4,3],[8,5],[5,8],[1,1],[0,6],[7,5],[1,6],[1,9],[9,4],[2,8],[1,3],[4,2],[2,5],[4,1],[0,2],[6,5]]
print(main(stones))
# print(countStones(stones))