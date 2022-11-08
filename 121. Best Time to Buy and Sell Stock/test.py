def main(prices):
    profit = 0
    vj = ij = 0
    for i in range(len(prices)-1):
        if prices[i] >= prices[i+1]:
            continue
        if ij <= i:
            vj = 0
            for j in range(len(prices)-1,  i, -1):
                if prices[j] > vj:
                    vj = prices[j]
                    ij = j
        for q in range(i, ij):
            if prices[i] >= prices[q]:
                i = q
        if profit < vj - prices[i]:
            profit = vj - prices[i]
    return profit


prices = [3,3,5,0,0,3,1,4]
print(main(prices))