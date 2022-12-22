class Solution:
    def longestPalindrome(self, s: str) -> str:
        letras = [s[0]]
        res = s[0]

        i = 1
        while i < len(s):
            for j in range(min(len(letras), len(s)-i)):
                if letras[j] == s[i+j]:
                    if len(res) < (j+1)*2:
                        res = s[i-j-1:i+j+1]
                else:
                    break
            
            for j in range(1, min(len(letras), len(s)-i+1)):
                if letras[j] == s[i+j-1]:
                    if len(res) < j*2+1:
                        res = s[i-j-1:i+j]
                else:
                    break

            letras.insert(0, s[i])
            i += 1
        
        return res