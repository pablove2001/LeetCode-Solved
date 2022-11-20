# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        v = set()
        if root.val == l[0]:
            v.add(0)
        return findList(root.left, l, v) or findList(root.right, l, v)
        
def findList(root, l, v):
    if len(l) == 1:
        return True
    if not root:
        return False
    nv = set()
    for i in v:
        if l[i+1] == root.val:
            if i+1 >= len(l)-1:
                return True
            nv.add(i+1)
    if root.val == l[0]:
        nv.add(0)
    return findList(root.left, l, nv) or findList(root.right, l, nv)