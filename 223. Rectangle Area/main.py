class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        aa = abs((ax1-ax2)*(ay1-ay2))
        ab = abs((bx1-bx2)*(by1-by2))

        if (ax1 <= bx1 <= ax2 or ax1 <= bx2 <= ax2 or bx1 <= ax1 <= bx2 or bx1 <= ax2 <= bx2) and (ay1 <= by1 <= ay2 or ay1 <= by2 <= ay2 or by1 <= ay1 <= by2 or by1 <= ay2 <= by2):
            x1 = max(ax1, bx1)
            x2 = min(ax2, bx2)
            y1 = max(ay1, by1)
            y2 = min(ay2, by2)
            return aa+ab-abs((x1-x2)*(y1-y2))
        return aa+ab
