class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        ml = len(m)-1 #matrixLen
        
        for r in range((len(m)+1)//2):
            for c in range(len(m)//2):
                m[r][c], m[c][ml-r], m[ml-r][ml-c], m[ml-c][r] = m[ml-c][r], m[r][c], m[c][ml-r], m[ml-r][ml-c]