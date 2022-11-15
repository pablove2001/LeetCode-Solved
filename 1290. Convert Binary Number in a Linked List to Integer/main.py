# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = ''
        while head != None:
            num += str(head.val)
            head = head.next
        res = 0
        for i in range(len(num)):
            if num[i] == '1':
                res += 2**(len(num)-i-1)
        return res
        