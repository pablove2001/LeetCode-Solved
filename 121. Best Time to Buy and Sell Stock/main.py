class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        vj = ij = 0
        for i in range(len(prices)-1):
            if prices[i] > prices[i+1]:
                continue
            if ij <= i:
                vj = 0
                for j in range(i+1, len(prices)):
                    if prices[j] >= vj:
                        vj = prices[j]
                        ij = j
            if profit < vj - prices[i]:
                profit = vj - prices[i]
            #print(f'v1: {prices[i]} i1: {i} -- v2: {vj} i2: {ij}')
        return profit