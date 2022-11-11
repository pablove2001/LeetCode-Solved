
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    values = getVal(root, [])
    for i in range(len(values)-1):
        if values[i] >= values[i+1]:
            return False
    return True


def getVal(root, values):
    if root.left != None:
        values = getVal(root.left, values)
    values.append(root.val)
    if root.right != None:
        values = getVal(root.right, values)
    return values


root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


print(isValidBST(root))

# for i in [5,1,4,3,6]:
#     print(f'i={i}, state={findVal(root, i)}')

# print(main(root))
