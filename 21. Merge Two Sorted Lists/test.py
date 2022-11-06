class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printNode(node):
    while node != None:
        print(node.val)
        node = node.next


p1i = ListNode(1)
p10 = p1i
p10.next = ListNode(2)
p10 = p10.next
p10.next = ListNode(4)

printNode(p1i)