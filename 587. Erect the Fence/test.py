def compare_slopes(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2) 


p1 = [1,1]
p2 = [2,0]
p3 = [2,2]

print(compare_slopes(p2,p3, p1))