# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        if not head:
            return head
        
        res = ListNode(head.val)
        p = res
        head = head.next
        
        while head:
            if head.val != val:
                p.next = ListNode(head.val)
                p = p.next
            head = head.next
        
        return res  