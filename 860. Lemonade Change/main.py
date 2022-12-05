class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        m5 = 0
        m10 = 0
        
        for i in bills:
            if i == 5:
                m5 += 1
            elif i == 10:
                if m5 >= 1:
                    m5 -= 1
                    m10 += 1
                else:
                    return False
            else:
                if m5 >= 1:
                    if m10 >= 1:
                        m10 -= 1
                        m5 -= 1
                    elif m5 >= 3:
                        m5 -= 3
                    else:
                        return False
                else:
                    return False
        return True