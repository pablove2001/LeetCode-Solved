# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        arr = getArr(root)
        # print(arr)
        maxMitad = arr[0]
        mitad = arr[-1]/2

        for i in range(len(arr)-1):
            if abs(mitad - arr[i]) < abs(mitad - maxMitad):
                maxMitad = arr[i]

        #print(maxMitad, arr[-1]-maxMitad)

        return (maxMitad * (arr[-1]-maxMitad)) % (10**9 + 7)


def getArr(root):
    if not root:
        return None

    p1 = getArr(root.left)
    p2 = getArr(root.right)
    ares = []
    res = 0

    if p1:
        res += p1[-1]
        ares += p1
    if p2:
        res += p2[-1]
        ares += p2

    res += root.val
    ares += [res]
    return ares
