class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c1 = True
        c2 = True
        c3 = True

        if word[0].isupper():
            c2 = False

        else:
            c1 = False
            c3 = False

        for i in range(1, len(word)):
            if word[i].isupper():
                c2 = False
                c3 = False
            else:
                c1 = False

        return c1 or c2 or c3
