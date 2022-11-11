# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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
