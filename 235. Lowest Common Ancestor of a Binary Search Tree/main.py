# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        arr1 = getWay(root, p.val, []) + ['f']
        arr2 = getWay(root, q.val, []) + ['f']
        i = 0
        while True:
            if arr1[i] != arr2[i] or arr1[i] == 'f' or arr2[i] == 'f':
                return arr1[i-1]
            i += 1

def getWay(root, num, arr):
    if root == None:
        return []
    arr.append(root)
    if num < root.val:
        arr = getWay(root.left, num, arr)
    elif num > root.val:
        arr = getWay(root.right, num, arr)
    return arr