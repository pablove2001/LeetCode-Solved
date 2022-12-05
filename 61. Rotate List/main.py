# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        k = k % len(arr)
        arr = arr[-k:] + arr[:-k]
        
        res = ListNode(arr[0])
        nres = res
        for i in range(1, len(arr)):
            nres.next = ListNode(arr[i])
            nres = nres.next
        
        return res