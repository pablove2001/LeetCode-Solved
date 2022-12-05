class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split(' ')
        print(arr)
        for i in range(0, len(arr)-1):
            if arr[i][-1] != arr[i+1][0]:
                return False
        if arr[0][0] != arr[-1][-1]:
            return False
        
        return True