def main(coordinates):
    arrx = []
    arry = []
    for i in range(1,len(coordinates)-1):
        if coordinates[i][0] - coordinates[i+1][0] != difx or coordinates[i][1] - coordinates[i+1][1] != dify:
            return False
    return True
        



coordinates = [[0,0],[0,1],[0,-1]]
print(main(coordinates))