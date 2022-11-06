# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None and list2 != None:
            return list2 
        if list1 != None and list2 == None:
            return list1
        
        if list2.val > list1.val:
            p1 = list1
            p2 = list2
        else:
            p1 = list2
            p2 = list1

        res = p1

        last = None
        while p1 != None and p2 != None:
            if p2.val > p1.val:
                last = p1
                p1 = p1.next
            elif p2.val < p1.val:
                p1, p2 = self.insert(last, p2)
            else: #if val1 == val2
                p1, p2 = self.insert(p1, p2)
        if p1 == None:
            p1 = last
        else: 
            while p1.next != None:
                p1 = p1.next
        p1.next = p2
        return res

    def insert(self, p1, p2):
        save2 = p2.next
        p2.next = p1.next
        p1.next = p2
        p2 = save2
        p1 = p1.next
        return p1, p2