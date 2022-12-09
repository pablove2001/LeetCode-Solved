# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return maxDiff(root, root.val, root.val)

def maxDiff(root, mn, mx):
    if not root:
        return mx-mn
    
    mn = min(mn, root.val)
    mx = max(mx, root.val)

    return max(maxDiff(root.left, mn, mx), maxDiff(root.right, mn, mx))