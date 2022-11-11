# Definition for a binary tree node.d
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = getVal(root, set())
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

def getVal(root, values):
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

