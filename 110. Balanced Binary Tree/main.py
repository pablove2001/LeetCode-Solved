# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        b, c = isB(root)
        return b

def isB(root):
    if not root:
        return True, 0
    
    bl, cl = isB(root.left)
    br, cr = isB(root.right)
    
    if not bl or not br or abs(cl-cr) > 1:
        return False, 0
    
    return True, max(cl, cr) + 1