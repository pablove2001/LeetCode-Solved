class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)//2
        vowles =  {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a = b = 0
        
        for i in range(l):
            if s[i] in vowles:
                a += 1
            if s[i+l] in vowles:
                b += 1

        if a == b:
            return True
        return False