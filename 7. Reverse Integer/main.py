class Solution:
    def reverse(self, x: int) -> int:
        menor = False
        if x < 0:
            menor = True
            x = abs(x)

        x = int(''.join(reversed(list(str(x)))))

        if menor:
            x = -x
        
        if -2**31 <= x <= 2**31-1:
            return x
        return 0