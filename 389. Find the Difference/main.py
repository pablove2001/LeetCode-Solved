class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lista = list(s)
        for c in t:
            if c in lista:
                lista.pop(lista.index(c))
            else:
                return c