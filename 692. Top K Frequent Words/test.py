class Solution:
    def topKFrequent(self, words: List[str], n: int) -> List[str]:
        m = {}
        for w in words:
            m[w] = m.get(w, 0) + 1

        arr = []
        for k, v in m.items():
            arr.append([v, k])

        return arr


def sortArr(arr):
