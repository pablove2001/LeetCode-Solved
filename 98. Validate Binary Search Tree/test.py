
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def main(root):
    values = getVal(root)
    if 'f' in values:
        return False
    for val in values:
        if not findVal(root, val):
            return False
    return True

def findVal(root, val):
    if val < root.val:
        if root.left != None:
            return findVal(root.left, val)
        return False
    if val > root.val:
        if root.right != None:
            return findVal(root.right, val)
        return False
    return True

# def getVal(root):
#     val = {root.val}
#     if root.left != None:
#         val = val.union(getVal(root.left)) 
#     if root.right != None:
#         val = val.union(getVal(root.right)) 
#     return val

def getVal(root, values=set()):
    if root.val in values or 'f' in values:
        values.add('f')
        return values
    else:
        values.add(root.val)
    if root.left != None:
        values = values.union(getVal(root.left, values)) 
    if root.right != None:
        values = values.union(getVal(root.right, values))
    return values
    

    

        




root = TreeNode(5)
root.left = TreeNode(6)
root.right = TreeNode(6)
root.right.left = TreeNode(6)
root.right.right = TreeNode(6)


print(getVal(root))

# for i in [5,1,4,3,6]:
#     print(f'i={i}, state={findVal(root, i)}')

# print(main(root))
