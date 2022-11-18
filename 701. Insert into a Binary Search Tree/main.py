# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        insertTree(root, val)
        return root

def insertTree(root, val):
    if val < root.val:
        if root.left: 
            insertTree(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right: 
            insertTree(root.right, val)
        else:
            root.right = TreeNode(val)