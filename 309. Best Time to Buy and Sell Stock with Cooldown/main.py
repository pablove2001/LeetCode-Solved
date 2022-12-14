class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        toBuy = 0
        toSell = cooldown = float('-inf')
        for p in prices:
            toBuy, toSell, cooldown = max(toBuy, cooldown), max(toSell, toBuy - p), toSell + p
        return max(toBuy, cooldown)