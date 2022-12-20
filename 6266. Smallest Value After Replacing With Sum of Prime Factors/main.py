class Solution:
    def smallestValue(self, n: int) -> int:
        pas = n
        res = sumPrimeFactors(pas)
        while res != pas:
            pas = res
            res = sumPrimeFactors(res)
        return res
    
def sumPrimeFactors(n):
    res = 0
    while n % 2 == 0:
        res += 2
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            res += int(i)
            n = n / i
    if n > 2:
        res += int(n)
    return res