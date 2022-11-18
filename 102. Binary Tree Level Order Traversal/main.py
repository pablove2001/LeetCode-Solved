# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        lv = 0
        arr = []
        return level(root, lv, arr)

def level(root, lv, arr):
    if not root:
        return arr
    if len(arr) == lv:
        arr.append([])
    arr[lv].append(root.val)
    arr = level(root.left, lv+1, arr)
    arr = level(root.right, lv+1, arr)
    return arr