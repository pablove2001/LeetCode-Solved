class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
            
        for i in range(len(words)):
            l = set(words[i])
            words[i] = ''.join(sorted(l))
            
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] == words[j]:
                    count += 1
   
        return count