def main(root, lev = 0, arr = []):
    if root == None: return arr
    if len(arr) == lev:
        arr.append([])
    arr[lev].append(root.val)

    if root.left:
        arr = main(root.left, lev+1, arr)
    if root.right:
        arr = main(root.rigth, lev+1, arr)
    return arr

root = []
main(root)