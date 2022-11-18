class Solution:
    def topKFrequent(self, words: List[str], n: int) -> List[str]:
        m = {}
        res = []
        for w in words:
            m[w] = m.get(w, 0) + 1

        arr = []
        for k, v in m.items():
            arr.append([k, v])
        
        for i in range(n):
            mk = ''
            mv = 0
            ind = 0
            for j in range(len(arr)):
                if arr[j][1] > mv:
                    mv = arr[j][1]
                    mk = arr[j][0]
                    ind = j
                elif arr[j][1] == mv:
                    if arr[j][0] < mk:
                        mv = arr[j][1]
                        mk = arr[j][0]
                        ind = j
            res.append(mk)
            arr.pop(ind)

        return res