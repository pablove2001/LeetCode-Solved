class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        m = Counter(magazine)
        
        for c, cnt in rn.items():
            if m.get(c, 0) < cnt:
                return False
        
        return True     