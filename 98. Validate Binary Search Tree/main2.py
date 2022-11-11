def isValidBST(root):
    values = getVal(root, [])

    return True

def getVal(root, values):
    if root.left != None:
        values = getVal(root.left, values)
    if root.right != None:
        values = values.union(getVal(root.right, values))
    return values

