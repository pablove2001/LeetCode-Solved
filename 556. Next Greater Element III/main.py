class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n > 2147483647:
            return -1
    
        num = list(str(n))[::-1]
        l = []
        
        for i in range(len(num)-1):
            l.append(num[i])
            if num[i] > num[i+1]:
                l.sort()
                for j in l:
                    if j > num[i+1]:
                        l.append(num[i+1])
                        num[i+1] = j
                        l.remove(j)
                        l.sort()
                        n = int("".join(reversed(l[::-1]+num[i+1:])))
                        if n > 2147483647:
                            return -1
                        return n
        return -1