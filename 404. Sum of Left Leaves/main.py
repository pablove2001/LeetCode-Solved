# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return nextChild(root.left, True) + nextChild(root.right, False)

def nextChild(root, isLeft):
    if not root:
        return 0
    if noChild(root) and isLeft:
        return root.val
    return nextChild(root.left, True) + nextChild(root.right, False)
    
def noChild(root):
    if root.left or root.right:
        return False
    return True
    