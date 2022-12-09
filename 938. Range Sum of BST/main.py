# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def toArr(root):
            if not root:
                return []
            return toArr(root.left) + [root.val] + toArr(root.right)
        
        arr = toArr(root)
        res = 0
        for i in arr:
            if i >= low:
                if i > high:
                    return res
                res += i

        return res
    
