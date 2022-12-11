# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = treeToLeaves(root1)
        arr2 = treeToLeaves(root2)

        return arr1 == arr2


def treeToLeaves(root):
    arr = []
    if root.left:
        arr += treeToLeaves(root.left)
    if root.right:
        arr += treeToLeaves(root.right)
    if not arr:
        return [root.val]
    return arr
