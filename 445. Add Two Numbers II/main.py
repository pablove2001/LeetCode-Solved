# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = ''
        r2= ''
        while l1:
            r1 = r1 + str(l1.val)
            l1 = l1.next
        
        while l2:
            r2 = r2 + str(l2.val)
            l2 = l2.next
        
        lr = list(map(int, list(str(int(r1)+int(r2)))))
        
        res = ListNode(lr[0])
        nres = res
        for i in range(1,len(lr)):
            nres.next = ListNode(lr[i])
            nres = nres.next
            
        return res