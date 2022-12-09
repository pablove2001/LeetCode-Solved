# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        p1 = ListNode(head.val)
        p2 = ListNode(head.next.val)
        ip1 = p1
        ip2 = p2

        head = head.next.next

        i = 0
        while head:
            if i % 2 == 0:
                p1.next = ListNode(head.val)
                p1 = p1.next
            else:
                p2.next = ListNode(head.val)
                p2 = p2.next
            head = head.next
            i += 1
        
        p1.next = ip2

        return ip1