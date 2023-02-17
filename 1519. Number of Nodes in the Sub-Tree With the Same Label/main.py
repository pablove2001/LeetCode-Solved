class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        connections = defaultdict(list)
        res = [0]*n

        for v1, v2 in edges:
            connections[v1].append(v2)
            connections[v2].append(v1)

        def solution(root):  # index, ..., ...
            if not connections[root]:
                res[root] = 1
                return Counter(labels[root])

            count = Counter()

            for i in connections[root]:
                connections[i].remove(root)
                count += solution(i)

            count.update(labels[root])
            res[root] = count[labels[root]]

            return count

        solution(0)

        return res
