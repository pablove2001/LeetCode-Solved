class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a = Counter(word1) 
        b = Counter(word2)
        
        if a.keys() != b.keys():
            return False

        if sorted(a.values()) != sorted(b.values()):
            return False
        
        return True