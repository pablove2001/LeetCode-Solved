class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        current = values[0]
        mx = 0

        for i in range(1, len(values)):
            current -= 1
            mx = max(mx, current+values[i])
            current = max(current, values[i])

        return mx
