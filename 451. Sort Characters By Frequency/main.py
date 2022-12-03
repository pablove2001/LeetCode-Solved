class Solution:
    def frequencySort(self, s: str) -> str:
        l = list(s)
        c = Counter(l)
        l.sort()
        l.sort(key=lambda x: c[x], reverse=True)
        return "".join(l)