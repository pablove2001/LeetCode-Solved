# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = bstToArr(root, [])
        p1 = 0
        p2 = len(arr)-1
        while p1 < p2:
            if arr[p1] + arr[p2] > k:
                p2 -= 1
            elif arr[p1] + arr[p2] < k:
                p1 += 1
            else:
                return True
        return False
    
def bstToArr(root, arr):
    if not root:
        return arr
    arr = bstToArr(root.left, arr)
    arr.append(root.val)
    return bstToArr(root.right, arr)