# Definition for a binary tree node.d
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = toArr(root, [])
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        return True
        
def toArr(root, arr):
    if not root:
        return arr
    arr = toArr(root.left, arr)
    arr.append(root.val)
    return toArr(root.right, arr)
    