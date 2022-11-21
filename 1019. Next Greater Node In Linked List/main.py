# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []
        
        i = 0
        while head:
            ans.append(0)
            while stack and stack[-1][1] < head.val:
                ind, v = stack.pop()
                ans[ind] = head.val
            
            stack.append([i, head.val])
            i += 1
            head = head.next
        
        return ans