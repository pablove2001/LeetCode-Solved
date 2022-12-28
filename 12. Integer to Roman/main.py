class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], ['', 'M', 'MM', 'MMM']]

        res = ''
        
        for i in range(3, -1, -1):
            res += symbol[i][int(num / 10**i)]
            num = num % 10**i

        return res