class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for w, l in matches:
            d[w] = d[w] + 0
            d[l] = d[l] + 1
        winner = []
        loser = []
        for p, l in d.items():
            if l == 0:
                winner.append(p)
            if l == 1:
                loser.append(p)
        winner.sort()
        loser.sort()
        return [winner, loser]