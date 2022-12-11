class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        current = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < current:
                current = prices[i]
            elif prices[i] > current:
                res += prices[i] - current
                current = prices[i]

        return res
