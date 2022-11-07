
def main(head):
    m = head
    while head.next != None:
        m = m.next
        head = head.next
        if head.next == None:
            return m
        head = head.next
    
    return m


head = []

main(head)