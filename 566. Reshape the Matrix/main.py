
def main(mat, r, c):
    if len(mat)*len(mat[0]) != r*c:
        return mat
    
    values = []
    for ir in range(len(mat)):
        for ic in range(len(mat[0])):
            values.append(mat[ir][ic])
    
    res = []
    for ir in range(r):
        res.append(values[(c*ir):(c*ir+c)])
    
    return res

    

    

    

mat = [[1,2],[3,4]]
r = 1
c = 4

print(main(mat, r, c))