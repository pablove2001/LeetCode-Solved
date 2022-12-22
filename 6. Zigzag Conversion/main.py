class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = ['' for _ in range(numRows)]
        
        modulo = numRows + max(numRows-2, 0)
        for i in range(len(s)):
            lugar = i%modulo
            if numRows <= lugar:
                lugar = numRows - ((lugar%numRows) + 1)-1
            arr[lugar] += s[i]
        
        return ''.join(arr)