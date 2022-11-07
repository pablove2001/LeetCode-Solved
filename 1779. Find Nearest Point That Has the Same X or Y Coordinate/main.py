def main(x, y, points):
    index = -1
    min = None

    for i in range(len(points)):
        if points[i][0] == x:
            dif = abs(points[i][1] - y)
            if min == None:
                min = dif
                index = i
            elif dif < min:
                min = dif
                index = i

        elif points[i][1] == y:
            dif = abs(points[i][0] - x)
            if min == None:
                min = dif
                index = i
            elif dif < min:
                min = dif
                index = i

    return index





x, y = 1, 1

points = [[1,1],[1,1]]

print(main(x, y, points))