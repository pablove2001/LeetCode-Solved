class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            if wordMenorQue(words[i], words[i+1], order) != 1:
                return False
        return True

def wordMenorQue(w1, w2, order):
    for i in range(min(len(w1), len(w2))):
        comp = charMenorQue(w1[i], w2[i], order)
        if comp != 0:
            return comp
    if len(w1) <= len(w2):
        return 1
    return -1

def charMenorQue(char1, char2, order):
    if char1 == char2:
        return 0
    for i in order:
        if i == char1:
            return 1
        if i == char2:
            return -1
    return 0