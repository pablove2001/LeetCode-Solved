# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return funct(root, [])


def funct(root, arr):
    if not root:
        return arr

    arr.append(root.val)
    arr = funct(root.left, arr)

    return funct(root.right, arr)
