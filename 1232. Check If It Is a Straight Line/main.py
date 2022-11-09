class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        coordinates.pop(0)
        coordinates.pop(0)
        for x, y in coordinates:
            if (x0 - x1) * (y1 - y) != (x1 - x) * (y0 - y1):
                return False
        return True