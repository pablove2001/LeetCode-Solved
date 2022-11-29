# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return find(root.left, root.right)
            
def find(l, r):
    if not r and not l:
        return True
    if not r or not l:
        return False
    if r.val != l.val:
        return False
    return find(l.left, r.right) and find(l.right, r.left)
        